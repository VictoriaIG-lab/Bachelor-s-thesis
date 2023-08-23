from flask import Flask, render_template
from flask_security import Security
from flask_login import LoginManager
from cod_sursa.Business.Repositories import UserRepository
from cod_sursa.Business.Services.HomeworkService import HomeworkService
from cod_sursa.Business.Services.LessonService import LessonService
from cod_sursa.Business.Services.UserService import UserService
from cod_sursa.Data.Utils import LoginForm
from cod_sursa.Data.Utils import RegistrationForm
from cod_sursa.Presentation.Authentication import auth
from cod_sursa.Presentation.Homeworks import homeworks
from Presentation.Lessons import lessons
from Presentation.Compiler import compiler
from Presentation.Exercises import exercises
from flask_login import current_user

from flask_admin import Admin

from Presentation.AdminView.ExerciseView import ExerciseView

from cod_sursa import Data as user_exercise_difficulty, Data as user_homework_difficulty, \
    Data as user_elo_update
from Presentation.AdminView.UserView import UserView

from Presentation.AdminView.ChapterView import ChapterView

import cod_sursa.Data.Domain.ChapterLesson as chapter_lesson
from Presentation.AdminView.ChapterLessonView import ChapterLessonView

import cod_sursa.Data.Domain.ChapterExercise as chapter_exercise
from Presentation.AdminView.ChapterExerciseView import ChapterExerciseView

from Presentation.AdminView.LessonView import LessonView

import cod_sursa.Data.Domain.UserLessonDifficulty as user_lesson_difficulty
from Presentation.AdminView.UserLessonDifficultyView import UserLessonDifficultyView

from Presentation.AdminView.RoleView import RoleView

from Presentation.AdminView.UserExerciseDifficultyView import UserExerciseDifficultyView

from Presentation.AdminView.HomeworkView import HomeworkView

from Presentation.AdminView.UserHomeworkDifficultyView import UserHomeworkDifficultyView

from Presentation.AdminView.NotificationView import NotificationView

from Presentation.AdminView.UserEloUpdateView import UserEloUpdateView
from Presentation.Progress import progress

app = Flask(__name__)
app.register_blueprint(auth)
app.register_blueprint(lessons)
app.register_blueprint(compiler)
app.register_blueprint(exercises)
app.register_blueprint(progress)
app.register_blueprint(homeworks)

app.config['SECRET_KEY'] = 'super-secret'
app.config['SECURITY_REGISTERABLE'] = True
app.config['SECURITY_PASSWORD_SALT'] = b"xxx"
app.config['SECURITY_PASSWORD_HASH'] = "sha512_crypt"
app.config['SECURITY_REGISTER_URL'] = '/create_account'
app.config['SECURITY_LOGIN_TEMPLATE'] = 'security/register.html'
app.config['TEMPLATES_AUTO_RELOAD'] = True

login_manager = LoginManager()
login_manager.init_app(app)

admin = Admin(app, name="my app", template_mode="bootstrap3")
admin.add_view(UserView(User.User, User.db.db_session))
admin.add_view(RoleView(Role.Role, Role.db.db_session))
admin.add_view(
    UserLessonDifficultyView(user_lesson_difficulty.UserLessonDifficulty, user_lesson_difficulty.db.db_session))
admin.add_view(LessonView(Lesson.Lesson, Lesson.db.db_session))
admin.add_view(ChapterExerciseView(chapter_exercise.ChapterExercise, chapter_exercise.db.db_session))
admin.add_view(ChapterLessonView(chapter_lesson.ChapterLesson, chapter_lesson.db.db_session))
admin.add_view(ChapterView(Chapter.Chapter, Chapter.db.db_session))
admin.add_view(ExerciseView(Exercise.Exercise, Exercise.db.db_session))
admin.add_view(
    UserExerciseDifficultyView(user_exercise_difficulty.UserExerciseDifficulty, user_exercise_difficulty.db.db_session))
admin.add_view(HomeworkView(Homework.Homework, Homework.db.db_session))
admin.add_view(
    UserHomeworkDifficultyView(user_homework_difficulty.UserHomeworkDifficulty, user_homework_difficulty.db.db_session))
admin.add_view(NotificationView(Notification.Notification, Notification.db.db_session))
admin.add_view(UserEloUpdateView(user_elo_update.UserEloUpdate,user_elo_update.db.db_session))

_lesson_service = LessonService()
user_repository = UserRepository()
user_service = UserService()
security = Security(app, user_repository.get_user_datastore())


@app.route("/")
def index():
    if current_user.is_authenticated:
        current_lesson_id = _lesson_service.get_current_lesson()
        return render_template("dashboard.html", user=current_user, current_lesson_id=current_lesson_id)

    register_form = RegistrationForm()
    login_form = LoginForm()
    return render_template("register.html", login_form=login_form, register_form=register_form)


_homework_service = HomeworkService()

if __name__ == '__main__':
    app.run(debug=True)



