from flask import render_template, Blueprint

from cod_sursa.Business.Services.LessonService import LessonService
from cod_sursa.Business.Services.UserService import UserService
from cod_sursa.Data.Utils import RegistrationForm
from cod_sursa.Data.Utils import LoginForm

from flask_login import current_user, login_user, logout_user

from cod_sursa.Data import User

auth = Blueprint('auth', __name__, template_folder='templates')

user_service = UserService()
_lesson_service = LessonService()


@auth.route("/login", methods=['POST'])
def login():
    if current_user.is_authenticated:
        current_lesson_id = _lesson_service.get_current_lesson()

        return render_template("dashboard.html", current_lesson_id=current_lesson_id,
                               name=current_user.get_display_name())

    login_form = LoginForm()
    register_form = RegistrationForm()

    if login_form.validate_on_submit():
        user = User.query.filter_by(email=login_form.email.data).first()
        if user is None:
            return render_template("register.html", login_form=login_form, register_form=register_form)

        else:
            flag = user.check_password(login_form.password.data)

            if flag is False:
                return render_template("register.html", login_form=login_form, register_form=register_form)

            else:
                login_user(user)
                current_lesson_id = _lesson_service.get_current_lesson()
                return render_template("dashboard.html", current_lesson_id=current_lesson_id,
                                       name=current_user.get_display_name())

    else:
        return render_template("register.html", login_form=login_form, register_form=register_form)


@auth.route("/register", methods=['POST'])
def register():
    if current_user.is_authenticated:
        return render_template("dashboard.html")

    login_form = LoginForm()
    register_form = RegistrationForm()

    if register_form.validate_on_submit():
        if User.query.filter_by(email=register_form.email.data).first() is None:
            user_service.create_user(register_form.email.data,
                                     register_form.password.data,
                                     "user")
            login_user(User.query.filter_by(email=register_form.email.data).first())

            current_lesson_id = _lesson_service.get_current_lesson()

            return render_template("dashboard.html", current_lesson_id=current_lesson_id,
                                   name=current_user.get_display_name())
        else:
            return render_template("register.html", login_form=login_form, register_form=register_form)
    else:
        return render_template("register.html", login_form=login_form, register_form=register_form)


@auth.route("/logout", methods=['GET'])
def logout():
    current_user.is_authenticated = False
    user_service.logout_user(current_user)

    logout_user()
    login_form = LoginForm()
    register_form = RegistrationForm()
    return render_template("register.html", login_form=login_form, register_form=register_form)
