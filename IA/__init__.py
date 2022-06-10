from flask import Flask
from flask_sqlalchemy import SQLAlchemy
from flask_login import LoginManager
from flask_admin import Admin
from flask_migrate import Migrate
import json


app = Flask(__name__)
app.config.from_file("config.json", load=json.load)

db = SQLAlchemy(app)
login_manager = LoginManager(app)
migrate = Migrate(app, db)



from IA.bp.auth.routes import auth
from IA.bp.main.routes import main


app.register_blueprint(auth)
app.register_blueprint(main)

