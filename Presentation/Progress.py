import datetime
from flask import Blueprint, render_template
from flask_login import current_user
import json

from cod_sursa.Business.Services.UserService import UserService

progress = Blueprint('progress', __name__, template_folder='templates')

_user_service = UserService()


def datetime_converter_for_json(o):
    if isinstance(o, datetime.datetime):
        return o.__str__()


@progress.route("/progress", methods=['GET'])
def get_progress_page():
    return render_template("user_profile.html", user=current_user)


@progress.route("/progress/elo/user/<user_id>", methods=['GET'])
def get_elo_for_user(user_id):
    elo_user = _user_service.get_user_by_id(user_id).elo_rating
    response = {
        'value': elo_user,
    }
    return json.dumps(response), 200


@progress.route("/progress/resolved/<user_id>", methods=['GET'])
def get_resolved_by_now(user_id):
    all_of_them = _user_service.get_resolved_by_now(user_id)

    response = {
        'lessons': all_of_them[0],
        'exercises': all_of_them[1],
        'homeworks': all_of_them[2]
    }

    return json.dumps(response), 200


@progress.route("/progress/elo/evolution/<user_id>", methods=['GET'])
def get_elo_evolution(user_id):
    response = _user_service.get_elo_updates_for_user(user_id)
    return json.dumps(response, default=datetime_converter_for_json), 200
