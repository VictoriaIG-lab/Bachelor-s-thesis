from sqlalchemy import Column, Integer, ForeignKey, Float, Boolean
import Data.Persistance.database as db


class ChapterExercise(db.Base):
    __tablename__ = 'chapter_exercise'
    exercise_id = Column(Integer, ForeignKey("exercise.id"), primary_key=True)
    chapter_id = Column(Integer, ForeignKey("chapter.id"), primary_key=True)

    def __repr__(self):
        return self.chapter_id, self.exercise_id
