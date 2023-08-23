from flask_wtf import FlaskForm
from wtforms.validators import InputRequired, Email, Length
from wtforms import StringField, PasswordField, BooleanField


class LoginForm(FlaskForm):
    email = StringField('email', validators=[InputRequired(message="This field is required!"),
                                             Email(message="Not a valid mail!")])
    password = PasswordField('password', validators=[InputRequired(message="This field is required!")])
