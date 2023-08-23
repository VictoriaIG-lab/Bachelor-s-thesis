from Business.Repositories.UserRepository import UserRepository
from Business.Repositories.LessonRepository import LessonRepository
from Business.Repositories.ExerciseRepository import ExerciseRepository
from Data.Domain.UserExerciseDifficulty import UserExerciseDifficulty
from Data.Persistance.database import db_session
import elo, math


class EloRatingRepository:
    _user_repository = UserRepository()
    _lesson_repository = LessonRepository()
    _exercise_repository = ExerciseRepository()
    db_context = db_session

    def get_elo_ratings(self, winner, loser):
        return elo.rate_1vs1(elo.Rating(winner), elo.Rating(loser))

    def adjust_elo_rating_for_functions(self, winner, loser, test_case_factor):
        """
        This will adjust the elo rating of the entities when we are dealing with functions
        that need to be tested using different test cases.
        Example: in case an user does 9/10 tests, it wouldn't be fair if he totally loses,
        and the lesson wins. It must be adjusted
        using the ratio of test cases resolved as a proportion.

        :param winner: input elo of winner
        :param loser: input elo of loser
        :param test_case_factor: how many test cases there were completed
        :return:
        """
        default_elo = self.get_elo_ratings(winner, loser)

        new_elo_winner = default_elo[0]
        new_elo_loser = default_elo[1]

        default_gained_elo_points = math.fabs(winner - default_elo[0])

        new_elo_winner = winner + default_gained_elo_points - (default_gained_elo_points * test_case_factor)
        new_elo_loser = loser - default_gained_elo_points + (default_gained_elo_points * test_case_factor)

        return new_elo_winner, new_elo_loser

    def lesson_wins_over_user(self, lesson_id, test_case_factor):
        user = self._user_repository.get_user_by_id(self._user_repository.get_current_user_id())
        lesson_for_user = self._lesson_repository.get_user_lesson_difficulty_for_user(lesson_id, user.id)
        lesson_title = self._lesson_repository.get_lesson_by_id(lesson_for_user.lesson_id).title

        if not lesson_for_user.is_completed():

            lesson_old_elo = lesson_for_user.elo_rating
            user_old_elo = user.elo_rating

            new_lesson_elo, new_user_elo = self.get_elo_ratings(lesson_old_elo, user_old_elo)

            if test_case_factor:
                new_lesson_elo, new_user_elo = self.adjust_elo_rating_for_functions(lesson_old_elo, user_old_elo,
                                                                                     test_case_factor)

            user_elo_difference = new_user_elo - user_old_elo
            self._user_repository.add_user_elo_update_entry(user.id, user_elo_difference,
                                                            "Lesson {}".format(lesson_title))

            user.elo_rating = new_user_elo
            lesson_for_user.elo_rating = new_lesson_elo

            self.db_context.commit()

    def user_wins_over_lesson(self, lesson_id):
        user = self._user_repository.get_user_by_id(self._user_repository.get_current_user_id())
        lesson_for_user = self._lesson_repository.get_user_lesson_difficulty_for_user(lesson_id, user.id)
        lesson_title = self._lesson_repository.get_lesson_by_id(lesson_for_user.lesson_id).title

        old_user_elo = user.elo_rating
        if not lesson_for_user.completed:
            new_user_elo, new_lesson_elo = self.get_elo_ratings(user.elo_rating, lesson_for_user.elo_rating)

            user_elo_difference = new_user_elo - old_user_elo

            self._user_repository.add_user_elo_update_entry(user.id, user_elo_difference,
                                                            "Lesson {}".format(lesson_title))

            user.elo_rating = new_user_elo
            lesson_for_user.elo_rating = new_lesson_elo

            lesson_for_user.completed = True

            self.db_context.commit()

    def exercise_wins_over_user(self, exercise_id, test_case_factor):
        user = self._user_repository.get_user_by_id(self._user_repository.get_current_user_id())
        exercise_for_user = self._exercise_repository.get_user_exercise_difficulty_for_user(exercise_id, user.id)
        exercise_title = self._exercise_repository.get_exercise_by_id(exercise_for_user.exercise_id).title

        exercise_old_elo = exercise_for_user.elo_rating
        user_old_elo = user.elo_rating

        if not exercise_for_user.completed:
            new_elo_exercise, new_elo_user = self.get_elo_ratings(exercise_for_user.elo_rating, user.elo_rating)

            if test_case_factor:

                new_elo_exercise, new_elo_user = self.adjust_elo_rating_for_functions(exercise_old_elo, user_old_elo,
                                                                                   test_case_factor)

            user_elo_difference = new_elo_user - user_old_elo
            self._user_repository.add_user_elo_update_entry(user.id,user_elo_difference,"Exercise {}".format(exercise_title))
            user.elo_rating = new_elo_user
            exercise_for_user.elo_rating = new_elo_exercise

        self.db_context.commit()

    def user_wins_over_exercise(self, exercise_id):
        user = self._user_repository.get_user_by_id(self._user_repository.get_current_user_id())
        exercise_for_user = self._exercise_repository.get_user_exercise_difficulty_for_user(exercise_id, user.id)
        exercise_title = self._exercise_repository.get_exercise_by_id(exercise_for_user.exercise_id).title

        user_old_elo = user.elo_rating
        exercise_old_elo = exercise_for_user.elo_rating

        if not exercise_for_user.completed:

            new_elo_user, new_elo_exercise = self.get_elo_ratings(user_old_elo,exercise_old_elo)

            user_elo_difference = new_elo_user - user_old_elo
            self._user_repository.add_user_elo_update_entry(user.id,user_elo_difference,"Exercise {}".format(exercise_title))

            user.elo_rating = new_elo_user
            exercise_for_user.elo_rating = new_elo_exercise
            exercise_for_user.completed = True

            self.db_context.commit()
