import datetime
from sqlalchemy import Column, Integer, ForeignKey, Float, Boolean, DateTime, String
from sqlalchemy.dialects.mysql import MEDIUMTEXT

import Data.Persistance.database as db

class UserEloUpdate(db.Base):
    __tablename__ = 'user_elo_update'
    id = Column(Integer(),primary_key=True)
    user_id = Column(Integer(),ForeignKey("user.id"))
    elo_difference = Column(Float())
    created_at = Column(DateTime, default=datetime.datetime.now())
    notes = Column(String(200))
