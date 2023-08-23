import time

from flask import Blueprint, render_template, request
import json

from cod_sursa.Business.Services.HomeworkService import HomeworkService
from cod_sursa.Business.Services.NotificationService import NotificationService

homeworks = Blueprint('homeworks', __name__, template_folder='templates')

_homework_service = HomeworkService()
_notification_service = NotificationService()


@homeworks.route("/homeworks", methods=['GET'])
def get_list_of_homeworks():
    list_homeworks = _homework_service.get_incomplete_homeworks_for_user()
    return render_template("list_of_homeworks.html", homeworks=list_homeworks)


@homeworks.route("/homeworks/<homework_id>", methods=['GET'])
def get_homeworks(homework_id):
    homework = _homework_service.get_homework_by_id(homework_id)
    temporary_code = _homework_service.get_temporary_code_for_homework(homework_id)
    homework_details = _homework_service.get_user_homework_difficulty_for_user(homework_id)
    return render_template("homework.html", homework=homework, temporary_code=temporary_code,
                           homework_details=homework_details)


@homeworks.route("/homeworks/test", methods=['POST'])
def test_homework():
    source_code = request.json['code']
    homework_id = request.json['id']

    execution_response = _homework_service.test_homework(source_code, homework_id)

    response = {
        'message': str(execution_response[0]),
        'code': str(execution_response[1])
    }

    return json.dumps(response), 200


@homeworks.route("/homeworks/submit", methods=['POST'])
def submit_homework():
    source_code = request.json['code']
    homework_id = request.json['id']

    execution_response = _homework_service.evaluate_homework(source_code, homework_id)

    response = {
        'message': str(execution_response[0]),
        'code': str(execution_response[1])
    }

    return json.dumps(response), 200


@homeworks.route("/notification_stream/<user_id>", methods=['GET'])
def notify(user_id):
    new_notifications = _notification_service.get_new_notification_for_user(user_id)
    if len(new_notifications) > 0:
        json_data = {}
        for notif in new_notifications:
            json_data[notif.id] = notif.content
        return json.dumps(json_data), 200

    return 'a', 404


@homeworks.route("/notification_stream/dismiss", methods=['POST'])
def dismiss_notifications():
    ids = request.json['ids']
    _notification_service.mark_notifications_as_seen(ids)
    return 'a',200

def update_remaining_time_for_lessons():
    current_date = time.strftime("%A, %d. %B %Y %I:%M:%S %p")
    print('[{}] Updating homeworks deadline...'.format(current_date))
    # TODO: update all uncompleted homeworks for all users and notify them
    _homework_service.reduce_points_and_days_for_lessons()
    current_date = time.strftime("%A, %d. %B %Y %I:%M:%S %p")
    print('[{}] Done!'.format(current_date))

# sched = BackgroundScheduler()
# sched.start()
# sched.add_job(update_remaining_time_for_lessons,
#               trigger=IntervalTrigger(seconds=10),
#               id = 'updating_homeworks_job',
#               replace_existing=True
#               )
# atexit.register(lambda : sched.shutdown())
