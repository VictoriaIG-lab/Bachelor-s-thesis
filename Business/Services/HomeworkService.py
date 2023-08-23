from flask_login import current_user

from Business.Repositories.HomeworkRepository import HomeworkRepository
from Business.Repositories.NotificationRepository import NotificationRepository
from Business.Repositories.UserRepository import UserRepository
from Business.Services.CompilerService import CompilerService


class HomeworkService:
    _homework_repository = HomeworkRepository()
    _compiler_service = CompilerService()
    _user_repository = UserRepository()
    _notification_repository = NotificationRepository()

    def get_homework_by_id(self, homework_id):
        return self._homework_repository.get_homework_by_id(homework_id)

    def get_incomplete_homeworks_for_user(self):
        '''

        :return: (user_homework_difficulty,homework)
        '''

        result = []

        incomplete_homweorks = self._homework_repository.get_incomplete_homeworks_for_user(current_user.id)

        for x in incomplete_homweorks:
            result.append((x, self._homework_repository.get_homework_by_id(x.homework_id)))

        return result

    def get_temporary_code_for_homework(self, homework_id):
        user_id = current_user.id
        return self._homework_repository.get_temporary_code_for_homework(user_id, homework_id)

    @staticmethod
    def get_test_case_factor_from_output(message):

        factor = message[len(message) - 4:]
        return int(factor[0]) / int(factor[2])

    def test_homework(self, source_code, homework_id):
        user_id = current_user.id
        homework = self._homework_repository.get_homework_by_id(homework_id)

        self._homework_repository.update_temporary_code(user_id, homework_id, source_code)

        result_from_execution = self._compiler_service.evaluate_function_submitted_by_user(source_code,
                                                                                              homework.test_cases)

        return result_from_execution

    def evaluate_homework(self, source_code, homework_id):

        user_id = current_user.id
        homework = self.get_homework_by_id(homework_id)
        user_homework_difficulty = self._homework_repository.get_homework_for_user(user_id, homework_id)

        self._homework_repository.update_temporary_code(user_id, homework_id, source_code)
        result_from_execution = self._compiler_service.evaluate_function_submitted_by_user(source_code,
                                                                                           homework.test_cases)

        # homework successfully compiled
        if result_from_execution[1] == 200:
            test_case_factor = self.get_test_case_factor_from_output(result_from_execution[0])

            # all tests are passed => homeworks is complete
            if test_case_factor == 1:
                self._user_repository.add_raw_elo_points_to_user(user_id, user_homework_difficulty.points)
                self._homework_repository.mark_homework_as_completed(homework_id, user_id)
            # not all tests passed => homework is incomplete
            else:
                addon_message = 'All tests must pass in order to complete the homework! \n' + result_from_execution[0]
                result_from_execution = (addon_message, result_from_execution[1])

        return result_from_execution

    def get_user_homework_difficulty_for_user(self,homework_id):
        return self._homework_repository.get_homework_for_user(current_user.id,homework_id)

    def reduce_points_and_days_for_lessons(self):
        all_users = self._user_repository.get_all_users()
        for user in all_users:
            homeworks = self._homework_repository.get_incomplete_homeworks_for_user(user.id)
            for homework in homeworks:
                message = self._homework_repository.reduce_remaining_time(homework.homework_id,user.id)
                self._notification_repository.create_notification_for_user(user.id,message)