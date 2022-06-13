from flask import render_template, redirect, url_for, abort, Blueprint, flash, request
from flask_login import login_user, logout_user, current_user, login_required
from IA.models import *
from IA.forms import *

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
    return render_template('users.html', users=members)


@main.route('/register')
def register():
    form = MemberForm()
    if form.validate_on_submit:
        pass
    return render_template("register.html", form=form)



