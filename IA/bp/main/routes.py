from flask import render_template, redirect, url_for, abort, Blueprint, flash, request
from flask_login import login_user, logout_user, current_user, login_required
from IA.models import *
from IA.forms import *
from IA import app

main = Blueprint('main', '__name__')


@main.route('/')
def index():
    if not current_user.is_authenticated:
        return redirect(url_for('auth.login'))
    return render_template('index.html')


# All users in datable.js
@main.route('/users')
def users():
    members = Member.query.order_by(Member.id.desc()).all()
    return render_template('users.html', users=members, app=app)


@main.route('/register', methods=["GET","POST"])
def register():
    form = MemberForm()
    url = url_for('form.register_member')
    
    return render_template("register.html",
                           form=form,
                           title="Kullanıcı Kayıt Formu",
                           url=url,
                           btn="Oluştur")

@main.route('/devices')
def devices():
    antenna_devices = AntennaDevice.query.all()
    return render_template('devices.html', antenna_devices=antenna_devices)


@main.route('/regions')
def regions():
    form = RegionForm()
    regions = Region.query.all()

    return render_template('regions.html', form=form, regions=regions)
