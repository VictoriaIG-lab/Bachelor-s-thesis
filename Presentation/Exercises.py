from flask import Blueprint, render_template, request
from flask_login import current_user
from cod_sursa.Business.Services.ExerciseService import ExerciseService
import json, elo

exercises = Blueprint('exercises', __name__, template_folder='templates')
_exercise_service = ExerciseService()


@exercises.route("/exercise/", methods=['GET'])
def suggest_exercise():
    exercise = _exercise_service.suggest_exercise_for_user(current_user.id)
    difficulty = elo.expect(current_user.elo_rating, exercise.default_elo_rating)

    temporary_code = _exercise_service.get_temporary_code(exercise.id)

    return render_template("exercise.html", exercise=exercise, difficulty=int(difficulty*100),temporary_code=temporary_code)


@exercises.route("/exercise/test", methods=['POST'])
def test_code():
    source_code = request.json['code']
    exercise_id = request.json['id']
    execution_response = _exercise_service.test_the_exercise(source_code, exercise_id)

    response = {
        'message': str(execution_response[0]),
        'code': str(execution_response[1])
    }
    return json.dumps(response), 200


@exercises.route("/exercise/submit", methods=['POST'])
def submit_code():
    source_code = request.json['code']
    exercise_id = request.json['id']
    execution_response = _exercise_service.evaluate_exercise(source_code, exercise_id)

    response = {
        'message': str(execution_response[0]),
        'code': str(execution_response[1])
    }
    return json.dumps(response), 200
