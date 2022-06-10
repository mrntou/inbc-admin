from flask import render_template, redirect, url_for, abort, Blueprint, flash, request
from flask_login import login_user, logout_user, current_user, login_required
from IA.models import User

main = Blueprint('main', '__name__')


@main.route('/')
def index():
    return render_template('index.html')