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
from IA.models import ApDevice, ModemDevice, AntennaDevice, Region


# SQLAlchemy Queries -- 

class Query:

    def modem(self):
        return ModemDevice.query
    def antenna(self):
        return AntennaDevice.query
    def region(self):
        return Region.query
    def ap(self):
        return ApDevice.query

query = Query()

class LoginForm(FlaskForm):
    username = StringField("Kullanıcı adı", validators=[DataRequired()])
    password = PasswordField("Parola", validators=[DataRequired()])
    remember = BooleanField("Beni Hatırla", default=False)
    submit = SubmitField("Giriş")



class MemberForm(FlaskForm):
    username = StringField(validators=[DataRequired()])
    name = StringField(validators=[DataRequired()])
    lastname = StringField(validators=[DataRequired()])
    phone_number = StringField(validators=[DataRequired()])
    # Device Information
    ipv4 = StringField(validators=[DataRequired()])
    mac = StringField()


    region = QuerySelectField(
        query_factory=query.region,
        allow_blank=False,
        get_label="region")

    antenna_device = QuerySelectField(
        query_factory=query.antenna,
        allow_blank=True,
        get_label="device_name")

    ap_device = QuerySelectField(
        query_factory=query.ap,
        allow_blank=False,
        get_label="device_username")

    modem_device = QuerySelectField(
        query_factory=query.modem,
        allow_blank=True,
        get_label="device_name")
    
    email = StringField()

    submit = SubmitField("Oluştur")


    