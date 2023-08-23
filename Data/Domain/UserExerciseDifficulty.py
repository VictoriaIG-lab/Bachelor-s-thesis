from sqlalchemy import Column, Integer, ForeignKey, Float, Boolean
from sqlalchemy.dialects.mysql import MEDIUMTEXT

import Data.Persistance.database as db


class UserExerciseDifficulty(db.Base):
    __tablename__ = 'user_exercise_difficulty'
    user_id = Column(Integer, ForeignKey("user.id"), primary_key=True)
    exercise_id = Column(Integer, ForeignKey("exercise.id"), primary_key=True)
    elo_rating = Column(Float(), nullable=False)
    completed = Column(Boolean(), default=False)
    temporary_code = Column(MEDIUMTEXT())

    def is_completed(self):
        return self.completed


