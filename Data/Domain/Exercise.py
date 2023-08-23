from sqlalchemy.orm import relationship
from Data.Domain.UserExerciseDifficulty import UserExerciseDifficulty
import Data.Persistance.database as db

from sqlalchemy import Column, Integer, String, Float

from sqlalchemy.dialects.mysql import MEDIUMTEXT


class Exercise(db.Base):
    __tablename__ = 'exercise'
    id = Column(Integer(),primary_key=True)
    title = Column(String(50))
    content = Column(MEDIUMTEXT())
    source_code = Column(MEDIUMTEXT())
    solved_source_code = Column(MEDIUMTEXT())
    default_elo_rating = Column(Float())

    user_exercise_difficulty = relationship(UserExerciseDifficulty,uselist=False)

