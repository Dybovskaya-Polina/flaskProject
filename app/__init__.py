import os
from flask_sqlalchemy import SQLAlchemy

from flask import Flask
from flask_wtf import CSRFProtect

basedir = os.path.abspath(os.path.dirname(__file__))

app = Flask(__name__)
app.config['SECRET_KEY'] = 'secret'
app.config['SQLALCHEMY_DATABASE_URI'] = 'mysql://root:@localhost/flask_db'
app.config['SQLALCHEMY_TRACK_MODIFICATIONS'] = False

csrf = CSRFProtect(app)
from flask_bootstrap5 import Bootstrap

bootstrap = Bootstrap(app)
db = SQLAlchemy(app)
from app import routes
