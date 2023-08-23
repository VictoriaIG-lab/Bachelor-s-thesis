from Business.Repositories.ExerciseRepository import ExerciseRepository
from Business.Repositories.HomeworkRepository import HomeworkRepository
from Business.Repositories.LessonRepository import LessonRepository
from Data.Persistance.database import *
from Data.Domain.User import User
from Data.Domain.Role import Role
from Data.Domain.UserEloUpdate import UserEloUpdate
from flask_security import SQLAlchemySessionUserDatastore
from flask_login import current_user


class UserRepository:
    __user_datastore = SQLAlchemySessionUserDatastore(db_session, User, Role)
    db_context = db_session

    _lesson_repository = LessonRepository()
    _exercise_repository = ExerciseRepository()
    _homework_repository = HomeworkRepository()


    def get_user_datastore(self):
        return self.__user_datastore

    def create_user(self, user):
        self.db_context.add(user)
        self.db_context.commit()

    def get_user_by_id(self, user_id):
        return User.query.filter(User.id == user_id).first()

    def get_current_user_id(self):
        if current_user.is_authenticated:
            return current_user.id
        else:
            return None

    def get_user_by_email(self,_email):
        return User.query.filter(User.email == _email).first()

    def add_raw_elo_points_to_user(self,user_id,raw_points):
        self.add_user_elo_update_entry(user_id,raw_points,"Homework!")

        usr = self.get_user_by_id(user_id)
        usr.elo_rating = usr.elo_rating + raw_points

        self.db_context.commit()

    def get_all_users(self):
        return User.query.all()

    def add_user_elo_update_entry(self,user_id,elo_difference,notes):
        user_elo_update = UserEloUpdate()
        user_elo_update.user_id = user_id
        user_elo_update.elo_difference = elo_difference
        user_elo_update.notes = notes

        self.db_context.add(user_elo_update)
        self.db_context.commit()


    def get_elo_progress_for_user(self,user_id):
        return UserEloUpdate.query.filter(UserEloUpdate.user_id == user_id).order_by(UserEloUpdate.created_at.asc()).all()

    def get_resolved_by_now(self,user_id):
        lessons = len(self._lesson_repository.get_all_completed_lessons_by_user(user_id))
        exercises = len(self._exercise_repository.get_all_exercises_completed_by_user(user_id))
        homeworks = len(self._homework_repository.get_all_completed_homeworks_for_user(user_id))

        return lessons, exercises, homeworks
