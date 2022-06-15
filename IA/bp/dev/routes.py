from flask import render_template, redirect, url_for, abort, Blueprint, flash, request
from flask_login import login_user, logout_user, current_user, login_required
from IA.models import *
from IA.forms import *

dev = Blueprint('dev', '__name__')


@dev.route('/delete/all_members')
def delete_all_members():
    members = Member.query.all()
    for x in members:
        db.session.delete(x)
    db.session.commit()
    flash("Tüm Kullanıcılar silindi ", "warning")
    return redirect(url_for('main.users'))

@dev.route('/add/members')
def add_members():
    import add_users_from_json
    flash("Tüm Kullanıcılar Eklendi ", "warning")

    return redirect(url_for('main.users'))
