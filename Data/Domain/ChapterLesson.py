from sqlalchemy import Column, Integer, ForeignKey
import Data.Persistance.database as db


class ChapterLesson(db.Base):
    __tablename__ = 'chapter_lesson'
    chapter_id = Column(Integer, ForeignKey("chapter.id"), primary_key=True)
    lesson_id = Column(Integer, ForeignKey("lesson.id"), primary_key=True)

    def __repr__(self):
        return self.chapter_id,self.lesson_id
