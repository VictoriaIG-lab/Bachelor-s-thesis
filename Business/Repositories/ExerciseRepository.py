from Data.Persistance.database import *
from Data.Domain.Exercise import Exercise
from Data.Domain.UserExerciseDifficulty import UserExerciseDifficulty
from Data.Domain.ChapterExercise import ChapterExercise
from flask_login import current_user


class ExerciseRepository:
    _db_context = db_session

    @staticmethod
    def get_exercise_by_id(_id):
        return Exercise.query.filter_by(id=_id).first()

    @staticmethod
    def get_all_exercises():
        return Exercise.query.all()

    @staticmethod
    def get_all_exercises_for_user(user_id):
        return UserExerciseDifficulty.query.filter_by(user_id=user_id).all()

    def get_all_unresolved_exercises_from_chapter(self, chapter_id):

        exercises_from_chapter = ChapterExercise.query.filter_by(chapter_id=chapter_id).all()
        list_of_exercises = []
        for exc in exercises_from_chapter:
            try:
                if not self.exercise_is_resolved_by_user(current_user.id, exc.exercise_id):
                    list_of_exercises.append(self.get_exercise_by_id(exc.exercise_id))
            except AttributeError:
                list_of_exercises.append(self.get_exercise_by_id(exc.exercise_id))

        return list_of_exercises

    def all_exercises_are_completed_by_user(self, user_id):

        exercises_for_user = self.get_all_exercises_for_user(user_id)
        total_exercises = self.get_all_exercises()

        if len(total_exercises) == len([exe for exe in exercises_for_user if exe.completed]):
            return True

        return False

    @staticmethod
    def exercise_is_resolved_by_user(user_id, exercise_id):
        return UserExerciseDifficulty.query.filter_by(user_id=user_id, exercise_id=exercise_id).first().completed

    @staticmethod
    def exercise_has_been_tried_before_by_user(user_id, exercise_id):
        obj = UserExerciseDifficulty.query.filter_by(user_id=user_id, exercise_id=exercise_id).first()
        if obj:
            return obj
        return False

    @staticmethod
    def get_user_exercise_difficulty_for_user(exercise_id, user_id):
        return UserExerciseDifficulty.query.filter_by(user_id=user_id, exercise_id=exercise_id).first()

    def create_user_exercise_difficulty_entry(self, exercise_id):
        user_id = current_user.id
        exercise = self.get_exercise_by_id(exercise_id)

        usr = UserExerciseDifficulty()
        usr.user_id = user_id
        usr.exercise_id = exercise_id
        usr.elo_rating = exercise.default_elo_rating
        usr.completed = False
        usr.temporary_code = exercise.source_code

        self._db_context.add(usr)
        self._db_context.commit()

    def update_temporary_code(self, user_id, exercise_id, source_code):
        usr_ex_diff = self.get_user_exercise_difficulty_for_user(exercise_id, user_id)

        usr_ex_diff.temporary_code = source_code

        self._db_context.commit()

    def get_temporary_code(self, user_id, exercise_id):
        usr_ex_diff = self.get_user_exercise_difficulty_for_user(exercise_id, user_id)
        return usr_ex_diff.temporary_code

    def get_all_exercises_completed_by_user(self,user_id):
        return UserExerciseDifficulty.query.filter_by(user_id=user_id,completed =1).all()

ex = ExerciseRepository()
