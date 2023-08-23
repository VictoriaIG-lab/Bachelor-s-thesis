import datetime
from sqlalchemy import Column, Integer, ForeignKey, Float, Boolean, DateTime
from sqlalchemy.dialects.mysql import MEDIUMTEXT

import Data.Persistance.database as db


class UserHomeworkDifficulty(db.Base):
    __tablename__ = 'user_homework_difficulty'
    user_id = Column(Integer, ForeignKey("user.id"), primary_key=True)
    homework_id = Column(Integer, ForeignKey("homework.id"), primary_key=True)
    points = Column(Integer())
    created_at = Column(DateTime, default=datetime.datetime.now())
    days_remaining = Column(Integer())
    expired = Column(Boolean(), default=False)
    completed = Column(Boolean(), default=False)
    temporary_code = Column(MEDIUMTEXT())
