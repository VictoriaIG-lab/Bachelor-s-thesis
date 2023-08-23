import Data.Persistance.database as db
from flask_security import UserMixin, RoleMixin
from sqlalchemy.orm import relationship, backref
from sqlalchemy import Boolean, DateTime, Column, Integer, \
    String, ForeignKey, Float

from Data.Domain.Role import Role
from Data.Domain.Notification import Notification

from flask.ext import bcrypt


class User(db.Base, UserMixin):
    __tablename__ = 'user'
    id = Column(Integer(), primary_key=True)
    name = Column(String(50))
    email = Column(String(100), unique=True)
    password = Column(String(512))
    elo_rating = Column(Float())
    active = Column(Boolean())
    role_id = Column(Integer(), ForeignKey('role.id'))
    role = relationship(Role)
    notification = relationship(Notification,uselist=False)
    is_authenticated = True

    def is_authenticated(self):
        return self.is_authenticated

    def is_active(self):
        return True

    def is_anonymous(self):
        return False

    def get_id(self):
        return self.id

    def check_password(self, input_password):
        return bcrypt.check_password_hash(self.password, input_password)

    def get_display_name(self):
        return self.email[:self.email.index('@')]
