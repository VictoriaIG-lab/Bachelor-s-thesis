from Data.Persistance.database import *
from Data.Domain.Homework import Homework
from Data.Domain.UserHomeworkDifficulty import UserHomeworkDifficulty


class HomeworkRepository:
    _db_context = db_session

    def get_homework_by_id(self, homework_id):
        return Homework.query.filter_by(id=homework_id).first()

    def get_homework_for_user(self, user_id, homework_id):
        return UserHomeworkDifficulty.query.filter_by(user_id=user_id, homework_id=homework_id).first()

    def get_incomplete_homeworks_for_user(self, user_id):
        return UserHomeworkDifficulty.query.filter(UserHomeworkDifficulty.user_id == user_id,
                                                   UserHomeworkDifficulty.completed == 0,
                                                   UserHomeworkDifficulty.expired == 0).order_by(
            UserHomeworkDifficulty.days_remaining.asc()).all()

    def update_temporary_code(self, user_id, homework_id, source_code):
        user_homework_difficulty = self.get_homework_for_user(user_id, homework_id)
        user_homework_difficulty.temporary_code = source_code
        self._db_context.commit()

    def get_temporary_code_for_homework(self, user_id, homework_id):
        return UserHomeworkDifficulty.query.filter_by(user_id=user_id, homework_id=homework_id).first().temporary_code

    def create_user_homework_difficulty_entry(self, user_id, homework_id):
        homework = self.get_homework_by_id(homework_id)

        new_entry = UserHomeworkDifficulty()
        new_entry.homework_id = homework_id
        new_entry.user_id = user_id
        new_entry.days_remaining = homework.days_available
        new_entry.temporary_code = ' '
        new_entry.points = homework.default_points

        self._db_context.add(new_entry)
        self._db_context.commit()

    def mark_homework_as_completed(self, homework_id, user_id):
        user_homework_difficulty = self.get_homework_for_user(user_id, homework_id)
        user_homework_difficulty.completed = True
        self._db_context.commit()

    def mark_homework_as_expired(self, homework_id, user_id):
        user_homework_difficulty = self.get_homework_for_user(user_id, homework_id)
        user_homework_difficulty.expired = True
        self._db_context.commit()

        return "{0} expired!".format(self.get_homework_by_id(user_homework_difficulty.homework_id).title)

    def reduce_remaining_time(self, homework_id, user_id):
        user_homework_difficulty = self.get_homework_for_user(user_id, homework_id)

        current_days_remaining = user_homework_difficulty.days_remaining

        if current_days_remaining == 1:
            return self.mark_homework_as_expired(homework_id, user_id)

        number_of_removing_points = 10
        user_homework_difficulty.days_remaining = current_days_remaining - 1
        user_homework_difficulty.points = user_homework_difficulty.points - number_of_removing_points

        self._db_context.commit()

        return "{0}: {1} remaining days!".format(self.get_homework_by_id(homework_id).title, current_days_remaining - 1)

    def get_all_completed_homeworks_for_user(self, user_id):
        return UserHomeworkDifficulty.query.filter_by(user_id=user_id, completed=1).all()


hwrepo = HomeworkRepository()
