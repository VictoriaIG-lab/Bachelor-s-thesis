import datetime
from sqlalchemy.orm import relationship
from Data.Domain.UserHomeworkDifficulty import UserHomeworkDifficulty
import Data.Persistance.database as db

from sqlalchemy import Column, Integer, String, Float, DateTime

from sqlalchemy.dialects.mysql import MEDIUMTEXT


class Homework(db.Base):
    __tablename__ = 'homework'
    id = Column(Integer(), primary_key=True)
    title = Column(String())
    content = Column(MEDIUMTEXT())
    days_available = Column(Integer())
    default_points = Column(Integer())
    test_cases = Column(MEDIUMTEXT())

    user_homework_difficulty = relationship(UserHomeworkDifficulty,uselist=False)
