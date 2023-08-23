from sqlalchemy import Column, Integer, String, Float
from sqlalchemy.orm import relationship, backref

import Data.Persistance.database as db
from sqlalchemy.dialects.mysql import MEDIUMTEXT

from Data.Domain.UserLessonDifficulty import UserLessonDifficulty
from Data.Domain.Chapter import Chapter


class Lesson(db.Base):
    __tablename__ = 'lesson'

    id = Column(Integer(), primary_key=True)
    title = Column(String(50))

    # the lesson's description and indications
    # such as: describing programming concepts, what is is used for, etc.
    content = Column(MEDIUMTEXT())

    # the keywords that must be used
    # programming specific instructions such as: 'print this thing, do this for, etc.'
    instructions = Column(MEDIUMTEXT())

    # starting source code of the lesson, that the user will complete on it
    source_code = Column(MEDIUMTEXT())

    user_lesson_difficulty = relationship(UserLessonDifficulty, uselist=False)

    default_elo_rating = Column(Float())

    foreign_keys=[]

    def is_completed(self):
        return self.user_lesson_difficulty.completed
