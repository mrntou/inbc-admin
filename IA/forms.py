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
from wtforms_sqlalchemy.fields import QuerySelectField
from IA.models import ModemDevice, AntennaDevice, Region


# SQLAlchemy Queries -- 

class Query:

    def modem(self):
        return ModemDevice.query
    def antenna(self):
        return AntennaDevice.query
    def region(self):
        return Region.query

query = Query()

class LoginForm(FlaskForm):
    username = StringField("Kullanıcı adı", validators=[DataRequired()])
    password = PasswordField("Parola", validators=[DataRequired()])
    remember = BooleanField("Beni Hatırla", default=False)
    submit = SubmitField("Giriş")



class MemberForm(FlaskForm):
    name = StringField(validators=[DataRequired()])
    lastname = StringField(validators=[DataRequired()])
    phone_number = StringField(validators=[DataRequired()])

    region = QuerySelectField(
        query_factory=query.region,
        allow_blank=False,
        get_label="region")

    antenna_device = QuerySelectField(
        query_factory=query.antenna,
        allow_blank=True,
        get_label="name")

    modem_device = QuerySelectField(
        query_factory=query.modem,
        allow_blank=True,
        get_label="name")
    
    email = StringField()


    