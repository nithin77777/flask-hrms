from wtforms import Form, Field, StringField, IntegerField, SubmitField, PasswordField

from wtforms.validators import InputRequired

class LoginForm(Form):
    username = StringField('Username', validators=[InputRequired()])
    password = PasswordField('Password', validators=[InputRequired()])
    submit = SubmitField('Log In')