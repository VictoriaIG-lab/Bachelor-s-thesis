from flask_login import current_user

from Data.Domain.Chapter import Chapter
from Data.Persistance.database import db_session
from Business.Repositories.LessonRepository import LessonRepository
from Data.Domain import UserLessonDifficulty as uld, ChapterLesson as cl
from statistics import mean


class ChapterRepository:
    db_context = db_session
    _lesson_repository = LessonRepository()

    def get_all_chapters(self):
        return Chapter.query.all()

    def get_chapter_by_id(self, _id):
        return Chapter.query.filter_by(id=_id).first()

    def get_lessons_by_chapter_id(self, chapter_id):
        chapter = self.get_chapter_by_id(chapter_id)

        chapter_and_lessons = cl.ChapterLesson.query.all()

        lessons = []

        for chls in chapter_and_lessons:
            if chls.chapter_id == chapter.id:
                lessons.append(self._lesson_repository.get_lesson_by_id(chls.lesson_id))

        return lessons

    def get_lessons_grouped_by_chapter_for_view(self):

        result = []
        user_id = current_user.id
        chapters = Chapter.query.all()
        chapter_and_lessons = cl.ChapterLesson.query.all()

        for chapter in chapters:

            a_chapter_with_lessons = [chapter]

            for chls in chapter_and_lessons:
                if chls.chapter_id == chapter.id:
                    lesson_completed_by_user = self._lesson_repository.lesson_is_completed_by_user(user_id,chls.lesson_id)
                    a_chapter_with_lessons.append((self._lesson_repository.get_lesson_by_id(chls.lesson_id),lesson_completed_by_user))

            result.append(a_chapter_with_lessons)

        current_lesson_id = self._lesson_repository.get_current_lesson_id_for_user(user_id)

        return result,current_lesson_id

    def get_max_of_elo_for_user(self, chapter_id, user_id):

        lessons = self.get_lessons_by_chapter_id(chapter_id)
        return max(
            [
                self._lesson_repository.get_elo_rating_of_lesson_for_given_user(lesson.id,user_id) - lesson.default_elo_rating
                for lesson in lessons
                if lesson.default_elo_rating - self._lesson_repository.get_elo_rating_of_lesson_for_given_user(lesson.id, user_id) < 0
             ]
        )

    def get_min_of_elo_for_user(self, chapter_id, user_id):
        lessons = self.get_lessons_by_chapter_id(chapter_id)
        return min(
            [
                self._lesson_repository.get_elo_rating_of_lesson_for_given_user(lesson.id, user_id) - lesson.default_elo_rating
                for lesson in lessons
                if lesson.default_elo_rating - self._lesson_repository.get_elo_rating_of_lesson_for_given_user(lesson.id, user_id) <= 0
            ]
        )

    def get_mean_of_elo_for_user(self, chapter_id, user_id):
        lessons = self.get_lessons_by_chapter_id(chapter_id)

        aux_list = []
        for lesson in lessons:
            new_elo_for_lesson_based_on_user_activity = self._lesson_repository.get_elo_rating_of_lesson_for_given_user(lesson.id,user_id)
            elo_difference = lesson.default_elo_rating - new_elo_for_lesson_based_on_user_activity

            if elo_difference <= 0:
                aux_list.append(elo_difference)
        try:
            return sum(aux_list)/len(aux_list)
        except ZeroDivisionError:
            return 0
        #
        #
        # return mean(
        #     [
        #         self._lesson_repository.get_elo_rating_of_lesson_for_given_user(lesson.id,user_id) - lesson.default_elo_rating
        #         for lesson in lessons
        #         if lesson.default_elo_rating - self._lesson_repository.get_elo_rating_of_lesson_for_given_user(lesson.id,user_id) <= 0
        #
        #      ]
        # )




