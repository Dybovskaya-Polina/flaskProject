
from flask import Flask

app = Flask(__name__)
from flask_bootstrap5 import Bootstrap
bootstrap = Bootstrap(app)

from app import routes
