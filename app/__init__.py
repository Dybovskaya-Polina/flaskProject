
from flask import Flask
from flask_wtf import CSRFProtect

app = Flask(__name__)
app.config['SECRET_KEY']='secret'
csrf = CSRFProtect(app)
from flask_bootstrap5 import Bootstrap
bootstrap = Bootstrap(app)

from app import routes
