from Business.Repositories.CompilerRepository import CompilerRepository
from Business.Repositories.EloRatingRepository import EloRatingRepository


def _format_output_error_message(message):
    return 'Error at: {}'.format(
        message.decode('utf-8')[len('  File "./script.py",'):])


class CompilerService:
    _compiler_repository = CompilerRepository()
    _elo_rating_repository = EloRatingRepository()

    def get_result_from_execution(self, source_code):

        result = self._compiler_repository.evaluate_simple_code_submission(source_code)

        # if the in stdout is empty that means the source code submitted has errors
        if not result[0] or not result[0].strip():
            return _format_output_error_message(result[1]), 500
        # else, the code has compiled and executed successfully
        else:
            return result[0].decode('utf-8'), 200

    def evaluate_submission(self, source_code, source_id):

        result = self.get_result_from_execution(source_code)

        if result[1] == 200:
            self._elo_rating_repository.user_wins_over_lesson(source_id)
        else:
            self._elo_rating_repository.lesson_wins_over_user(source_id, None)

        return result

    def evaluate_function_submitted_by_user(self, source_code, resolved_code):
        result = self._compiler_repository.evaluate_function_submitted_by_user(source_code, resolved_code)

        if not result[0] or not result[0].strip():
            return _format_output_error_message(result[1]), 500
            # else, the code has compiled and executed successfully
        else:
            return result[0].decode('utf-8'), 200
