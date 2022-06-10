from flask import render_template, redirect, url_for, abort, Blueprint, flash, request
from flask_login import login_user, logout_user, current_user, login_required
from IA.models import User
from IA.forms import LoginForm


auth = Blueprint("auth", __name__)



@auth.route('/login')
def login():
    if current_user.is_authenticated:
        return  "OK"
    form = LoginForm()

    if form.validate_on_submit():
        user = User.query.filter_by(username=form.username.data).first()
        if not user:
            flash("<b>Hata:</b> Kullanıcı adı veya şifre yalnış!", "danger")
            return redirect(request.url)

        if user and user.check_password(form.password.data):
            login_user(user, remember=form.remember.data, force=True)
            return redirect('Login OK')

        else:
            flash("<b>Hata:</b>Kullanıcı adı veya şifre yalnış!", "warning")
            return redirect(request.url)

    
    return render_template('login.html', form=form)