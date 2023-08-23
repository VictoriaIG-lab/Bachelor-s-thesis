from flask_login import current_user

from Business.Repositories.ExerciseRepository import ExerciseRepository
from Business.Repositories.ChapterRepository import ChapterRepository
from Business.Repositories.UserRepository import UserRepository
from Business.Services.CompilerService import CompilerService
from Business.Repositories.EloRatingRepository import EloRatingRepository
import random, elo


class ExerciseService:
    _exercise_repository = ExerciseRepository()
    _chapter_repository = ChapterRepository()
    _user_repository = UserRepository()
    _compiler_service = CompilerService()
    _elo_rating_repository = EloRatingRepository()

    def suggest_exercise_for_user(self, user_id):

        # if all the lessons are completed, then a random exercise from all the ones will be generated
        if self._exercise_repository.all_exercises_are_completed_by_user(user_id):
            all_exercises_id = [ex.id for ex in self._exercise_repository.get_all_exercises()]
            return self._exercise_repository.get_exercise_by_id(random.choice(all_exercises_id))

        # else, we will generate the possible exercises that the user should resolve, based on his progress

        all_chapters = self._chapter_repository.get_all_chapters()
        chapters_with_criteria = []

        for chapter in all_chapters:
            chapter_id = chapter.id

            # first we will take the exercises from the chapter which has the mean elo defined by lessons lesser than the others
            # we'll try it with the min or max or other selection method if we see it's not efficient

            mean_elo_chapter = self._chapter_repository.get_mean_of_elo_for_user(chapter_id, user_id)
            # min_elo_chapter = self._chapter_repository.get_min_of_elo_for_user(chapter_id, user_id)
            # max_elo_chapter = self._chapter_repository.get_max_of_elo_for_user(chapter_id, user_id)



            chapters_with_criteria.append(
                (chapter_id, mean_elo_chapter)
            )

        # sort ascending the chapters based on the criteria
        chapters_with_criteria.sort(key=lambda tup: tup[1])

        # TODO: find a treshold which will ignore the chapters, meaning that the user did well on that chapter and is not necessary for exercises
        treshold = 1000

        index = 0
        all_exercises = self._exercise_repository.get_all_unresolved_exercises_from_chapter(
            chapters_with_criteria[index][0])

        while len(all_exercises) == 0 and index < len(chapters_with_criteria):
            all_exercises = self._exercise_repository.get_all_unresolved_exercises_from_chapter(
                chapters_with_criteria[index][0])
            index = index + 1


        best_chance_to_win = (0, float('-inf'))
        user_elo = self._user_repository.get_user_by_id(user_id).elo_rating

        for exercise in all_exercises:
            chances_for_user_to_do_the_exercise = elo.expect(user_elo, exercise.default_elo_rating)
            if chances_for_user_to_do_the_exercise > best_chance_to_win[1]:
                best_chance_to_win = (exercise.id, chances_for_user_to_do_the_exercise)

        # exercise_to_be_recommended_id = 1
        exercise_to_be_recommended_id = best_chance_to_win[0]

        if not self._exercise_repository.exercise_has_been_tried_before_by_user(current_user.id,
                                                                                exercise_to_be_recommended_id):
            self._exercise_repository.create_user_exercise_difficulty_entry(exercise_to_be_recommended_id)

        return self._exercise_repository.get_exercise_by_id(exercise_to_be_recommended_id)

    @staticmethod
    def get_test_case_factor_from_output(message):

        factor = message[len(message) - 4:]
        return int(factor[0]) / int(factor[2])

    def test_the_exercise(self, source_code, exercise_id):
        user_id = current_user.id

        exercise = self._exercise_repository.get_exercise_by_id(exercise_id)


        self._exercise_repository.update_temporary_code(user_id,exercise_id,source_code)

        result_from_execution = self._compiler_service.evaluate_function_submitted_by_user(source_code,
                                                                                           exercise.solved_source_code)

        return result_from_execution

    def evaluate_exercise(self, source_code, exercise_id):
        user_id = current_user.id
        self._exercise_repository.update_temporary_code(user_id,exercise_id,source_code)

        exercise = self._exercise_repository.get_exercise_by_id(exercise_id)
        result_from_execution = self._compiler_service.evaluate_function_submitted_by_user(source_code,
                                                                                           exercise.solved_source_code)

        # the execution runs ok
        if result_from_execution[1] == 200:
            test_case_factor = self.get_test_case_factor_from_output(result_from_execution[0])

            # the user totally wins
            if test_case_factor == 1:
                self._elo_rating_repository.user_wins_over_exercise(exercise_id)

            # the user loses, even intermedially(the points will be given, for the test that he passed, but the exercise will not be marked as completed)
            else:
                self._elo_rating_repository.exercise_wins_over_user(exercise_id, test_case_factor)

        # the execution has errors, which means the user did not succeed the lesson
        else:
            self._elo_rating_repository.exercise_wins_over_user(exercise_id, None)

        return result_from_execution

    def get_temporary_code(self,exercise_id):
        return self._exercise_repository.get_temporary_code(current_user.id,exercise_id)
