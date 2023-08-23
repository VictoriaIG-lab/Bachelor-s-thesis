from flask_login import current_user

from Business.Repositories.LessonRepository import LessonRepository
from Business.Repositories.UserRepository import UserRepository
from Data.Domain.User import User
from Data.Domain.Role import Role
from flask.ext import bcrypt


class UserService:
    __user_repository = UserRepository()
    __lesson_repository = LessonRepository()

    def create_user(self, email, password, _role):
        user = User()
        user.email = email
        user.password = bcrypt.generate_password_hash(password)
        user.elo_rating = 1200

        role = Role()
        role.name = _role
        user.role = role

        self.__user_repository.create_user(user)
        self.__lesson_repository.assign_every_lesson_to_a_user(self.get_user_by_email(email).id)

    def logout_user(self,user):
        self.__user_repository.create_user(user)

    def get_user_by_id(self,user_id):
        return self.__user_repository.get_user_by_id(user_id)

    def get_current_user_id(self):
        return self.get_current_user_id()

    def get_user_by_email(self,_email):
        return self.__user_repository.get_user_by_email(_email)

    def get_elo_updates_for_user(self,user_id):
        response = self.__user_repository.get_elo_progress_for_user(user_id)
        result_list = []
        for x in response:
            result_list.append({
                'created_at' : x.created_at,
                'value' : x.elo_difference,
                'notes' : x.notes
            })

        return result_list

    def get_resolved_by_now(self,user_id):
        '''
        :return: (lessons,exercises,homeworks) => how many the user completed
        '''

        return self.__user_repository.get_resolved_by_now(user_id)


u = UserService()
