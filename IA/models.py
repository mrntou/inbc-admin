# Database for INBC-AMDIN users
from IA import app, db, login_manager
from flask_login import UserMixin, current_user
from werkzeug.security import generate_password_hash, check_password_hash


@login_manager.user_loader
def load_user(user_id):
    return User.query.get(user_id)


# INBC Admin Users -------------------------------------------------------
class User(UserMixin, db.Model):
    id = db.Column(db.Integer, primary_key=True)
    username = db.Column(db.String())
    email = db.Column(db.String())
    profile_image = db.Column(db.String(), default="user_default.png")
    is_admin = db.Column(db.Boolean, default=True)
    password_hash = db.Column(db.String())

    def __init__(self, username):
        self.username = username

    def set_password(self, password):
        self.password_hash = generate_password_hash(password)

    def check_password(self, password):
        return check_password_hash(self.password_hash, password)

    def __repr__(self):
        return f"<User> {self.username}"


# INBC Members --------------------------------------------------------
class Member(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    name = db.Column(db.String())
    lastname = db.Column(db.String())
    phone_number = db.Column(db.String())
    email = db.Column(db.String())

    # Relationships -
    region_id = db.Column(db.Integer, db.ForeignKey('region.id'))
    antenna_device_id = db.Column(db.Integer, db.ForeignKey('antenna_device.id'))
    modem_device_id = db.Column(db.Integer, db.ForeignKey('modem_device.id'))


    def _repr__(self):
        return f"<Member> {self.name} {self.lastname}"



class AntennaDevice(db.Model):
    __tablename__ = "antenna_device"
    id = db.Column(db.Integer, primary_key=True)
    device_name = db.Column(db.String())
    members = db.relationship('Member', backref='antenna_device', lazy=True)



class ModemDevice(db.Column):
    __tablename__ = "modem_device"
    id = db.Column(db.Integer, primary_key=True)
    device_name = db.Column(db.String())
    members = db.relationship('Member', backref='modem_device', lazy=True)

    


class Region(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    region = db.Column(db.String())
    members = db.relationship('Member', backref='region', lazy=True)

    



class Password(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    note = db.Column(db.String())
    user = db.Column(db.String())
    password = db.Column(db.String())



