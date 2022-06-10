from flask_wtf import FlaskForm
from flask_wtf.file import FileField, FileAllowed
from wtforms import (
    StringField,
    PasswordField,
    SubmitField,
    TextAreaField,
    SelectField,
    BooleanField,
    IntegerField,
)
from wtforms.validators import (
    DataRequired,
    Email,
    ValidationError,
    InputRequired,
    EqualTo,
    Length,
)


class LoginForm(FlaskForm):
    username = StringField("Kullanıcı adı", validators=[DataRequired()])
    password = PasswordField("Parola", validators=[DataRequired()])
    remember = BooleanField("Beni Hatırla", default=False)
    submit = SubmitField("Giriş")