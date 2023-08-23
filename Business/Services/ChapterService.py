from Business.Repositories.ChapterRepository import ChapterRepository

class ChapterService:

    _chapter_repository = ChapterRepository()

    def get_all_chapters(self):
        return self._chapter_repository.get_all_chapters()

    def get_chapter_by_id(self,_id):
        return self._chapter_repository.get_chapter_by_id(_id)

    def get_lessons_by_chapter(self):
       return self._chapter_repository.get_lessons_grouped_by_chapter_for_view()

