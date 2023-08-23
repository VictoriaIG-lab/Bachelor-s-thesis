from wtforms import Form, BooleanField, StringField, PasswordField
from wtforms.validators import InputRequired, Email, Length,EqualTo

from flask_wtf import FlaskForm


class RegistrationForm(FlaskForm):
    email = StringField('Email Address', [Length(max=100,message="Maximum 100 characters!"),
                                          InputRequired(message="This field is required!"),
                                          Email(message="Not a valid mail!")])
    password = PasswordField('New Password', [InputRequired(message="This field is required!"),
                                                EqualTo('confirm', message='Passwords must match')
    ])
    confirm = PasswordField('Repeat Password',[InputRequired(message="This field is required!")])
