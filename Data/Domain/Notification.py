import datetime
from sqlalchemy import Column, Integer, ForeignKey, DateTime, Boolean, String

import Data.Persistance.database as db


class Notification(db.Base):
    __tablename__ = 'notification'
    id = Column(Integer(),primary_key=True)
    user_id = Column(Integer,ForeignKey("user.id"),primary_key=True)
    created_at = Column(DateTime, default=datetime.datetime.now())
    content = Column(String(250),primary_key=True)
    seen = Column(Boolean(),default=False)

