from sqlalchemy import Column, Integer, ForeignKey, Float, Boolean
from sqlalchemy.dialects.mysql import MEDIUMTEXT

import Data.Persistance.database as db

class UserLessonDifficulty(db.Base):
    """
    Used to link a :class:`User` to a :class:`Lesson`
    and have a custom difficulty (Elo rating) between them

    Example: We want that each user to have the same lessons,
    but with different difficulty, customized by the user's progress so far.
    """

    __tablename__ = 'user_lesson_difficulty'
    user_id = Column(Integer, ForeignKey("user.id"), primary_key=True)
    lesson_id = Column(Integer, ForeignKey("lesson.id"), primary_key=True)
    elo_rating = Column(Float(), nullable=False)
    completed = Column(Boolean(), default=False)
    temporary_code = Column(MEDIUMTEXT())

    def is_completed(self):
        return self.completed
