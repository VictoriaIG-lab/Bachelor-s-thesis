from flask import Blueprint
from cod_sursa.Business import CompilerService

compiler = Blueprint('compiler', __name__)

_compiler_service = CompilerService()

#
# @compiler.route("/code/test", methods=['POST'])
# def lesson_test_code():
#     source_code = request.json['code']
#     execution_response = _compiler_service.get_result_from_execution(source_code)
#
#     response = {
#         'message': str(execution_response[0]),
#         'code': str(execution_response[1])
#     }
#     return json.dumps(response), 200
#
#
# @compiler.route("/code/submit", methods=['POST'])
# def lesson_submit_code():
#     source_code = request.json['code']
#     lesson_id = request.json['lesson_id']
#
#     execution_response = _compiler_service.evaluate_submission(source_code, lesson_id)
#
#     response = {
#         'message': str(execution_response[0]),
#         'code': str(execution_response[1])
#     }
#     return json.dumps(response), 200
