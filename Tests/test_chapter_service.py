from unittest import *

from Business.Services.ChapterService import ChapterService


class ChapterServiceTest(TestCase):

    def setUp(self):
        self.chapter_service = ChapterService()

    def tearDown(self):
        self.chapter_service = None

    def test_get_all_chapters(self):

        chapters = self.chapter_service.get_all_chapters()

        self.assertIsNotNone(chapters)

    def test_get_lessons_by_chapter(self):

        rez = self.chapter_service.get_lessons_grouped_by_chapter_for_view()

        self.assertIsNotNone(rez)

    def test_get_chapter_by_id(self):

        _id = 1

        chapter = self.chapter_service.get_chapter_by_id(_id)

        self.assertEquals(chapter.id,_id)