from flask_login import current_user

from Data.Persistance.database import *
from Data.Domain.Lesson import Lesson
from Data.Domain.UserLessonDifficulty import UserLessonDifficulty
from Data.Domain.ChapterLesson import ChapterLesson


class LessonRepository:
    _db_context = db_session

    def get_all_lessons(self):
        return Lesson.query.all()

    def get_lesson_by_id(self, lesson_id):
        return Lesson.query.filter_by(id=lesson_id).first()

    def get_lessons_ordered_by_id(self):
        return sorted(Lesson.query.all(), key=lambda a_lesson: a_lesson.id)

    def get_user_lesson_difficulty_for_user(self, lesson_id, user_id):
        return UserLessonDifficulty.query.filter_by(lesson_id=lesson_id, user_id=user_id).first()

    def get_elo_rating_of_lesson_for_given_user(self, lesson_id, user_id):
        return self.get_user_lesson_difficulty_for_user(lesson_id, user_id).elo_rating

    def mark_lesson_as_completed(self, lesson_id):
        lesson = self.get_lesson_by_id(lesson_id)
        lesson.user_lesson_difficulty.completed = 1
        self._db_context.commit()

    def assign_every_lesson_to_a_user(self, user_id):
        lessons = self.get_all_lessons()

        for lesson in lessons:
            user_difficulty = UserLessonDifficulty()

            user_difficulty.user_id = user_id
            user_difficulty.lesson_id = lesson.id
            user_difficulty.elo_rating = lesson.default_elo_rating
            user_difficulty.temporary_code = lesson.source_code

            self._db_context.add(user_difficulty)

        self._db_context.commit()

    def get_chapter_id_of_lesson(self, lesson_id):
        return ChapterLesson.query.filter_by(lesson_id=lesson_id).first().chapter_id

    def get_hard_lessons_for_user(self, user_id):

        all_lessons = self.get_all_lessons()

        hard_lessons = [lesson for lesson in all_lessons if
                        self.get_elo_rating_of_lesson_for_given_user(lesson.id, user_id) > lesson.default_elo_rating]

        return hard_lessons

    @staticmethod
    def lesson_is_completed_by_user(user_id, lesson_id):
        obj = UserLessonDifficulty.query.filter_by(user_id=user_id, lesson_id=lesson_id).first()
        if obj is None:
            return False
        elif obj.completed:
            return True
        return False

    def get_next_lesson(self, lesson_id):

        next_lesson = Lesson.query.filter(Lesson.id > lesson_id).first()

        if not next_lesson:
            return None
        return next_lesson

    def get_previous_lesson(self, lesson_id):
        previous_lesson = Lesson.query.filter(Lesson.id < lesson_id).order_by(Lesson.id.desc()).first()
        if not previous_lesson:
            return None
        return previous_lesson

    def get_current_lesson_id_for_user(self, user_id):
        '''

        :return: The lesson which the user is at the moment
        '''

        current_lesson = UserLessonDifficulty.query.filter(UserLessonDifficulty.completed == 0,
                                                           UserLessonDifficulty.user_id == user_id).order_by(
            UserLessonDifficulty.lesson_id.asc()).first()

        if current_lesson:
            return current_lesson.lesson_id
        return None

    def update_temporary_code(self, source_code, user_id, lesson_id):
        user_lesson_difficulty = UserLessonDifficulty.query.filter_by(user_id=user_id, lesson_id=lesson_id).first()

        user_lesson_difficulty.temporary_code = source_code

        self._db_context.commit()

    def get_temporary_code(self,user_id,lesson_id):
        user_lesson_difficulty = UserLessonDifficulty.query.filter_by(user_id=user_id, lesson_id=lesson_id).first()
        return user_lesson_difficulty.temporary_code

    def get_all_completed_lessons_by_user(self,user_id):
        return UserLessonDifficulty.query.filter_by(user_id=user_id,completed=1).all()


les = LessonRepository()
