from flask import Blueprint, render_template, request
from cod_sursa.Business import ChapterService
from cod_sursa.Business.Services.LessonService import LessonService
import json

lessons = Blueprint('courses', __name__, template_folder='templates')
_lesson_service = LessonService()
_chapter_service = ChapterService()


@lessons.route("/lessons", methods=['GET'])
def get_main_page():
    chapter_lessons = _chapter_service.get_lessons_by_chapter()

    return render_template("list_of_lessons.html", chapter_lessons=chapter_lessons)


@lessons.route("/lesson/<lesson_id>", methods=['GET'])
def get_lesson_by_id(lesson_id):
    lesson = _lesson_service.get_lesson_by_id(lesson_id)
    is_current_completed = _lesson_service.is_lesson_completed_by_user(lesson.id)

    previous_lesson = _lesson_service.get_previous_lesson(lesson_id)

    is_previous_completed = False
    if previous_lesson:
        is_previous_completed = _lesson_service.is_lesson_completed_by_user(previous_lesson.id)

    next_lesson = _lesson_service.get_next_lesson(lesson_id)
    is_next_completed = False
    if next_lesson:
        is_next_completed = _lesson_service.is_lesson_completed_by_user(next_lesson.id)


    temporary_code = _lesson_service.get_temporary_code(lesson_id)

    return render_template("lesson.html", lesson=lesson,
                           is_current_completed=is_current_completed,
                           previous_lesson=(previous_lesson, is_previous_completed),
                           next_lesson=(next_lesson, is_next_completed),
                           temporary_code=temporary_code)


@lessons.route("/lesson/completed/<lesson_id>", methods=['GET'])
def is_lesson_completed(lesson_id):
    completed = False

    try:
        completed = _lesson_service.is_lesson_completed_by_user(lesson_id).completed
    except:
        completed = False

    response = {
        'completed': completed
    }

    return json.dumps(response), 200


@lessons.route("/lesson/test", methods=['POST'])
def test_code():
    source_code = request.json['code']
    lesson_id = request.json['id']
    execution_response = _lesson_service.get_result_from_execution(source_code,lesson_id)

    response = {
        'message': str(execution_response[0]),
        'code': str(execution_response[1])
    }
    return json.dumps(response), 200


@lessons.route("/lesson/submit", methods=['POST'])
def submit_code():
    source_code = request.json['code']
    lesson_id = request.json['id']

    execution_response = _lesson_service.evaluate_submission(source_code, lesson_id)

    is_completed = _lesson_service.is_lesson_completed_by_user(lesson_id)

    response = {
        'message': str(execution_response[0]),
        'code': str(execution_response[1]),
        'completed': str(is_completed)
    }
    return json.dumps(response), 200
