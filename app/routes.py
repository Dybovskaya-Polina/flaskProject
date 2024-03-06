from flask import render_template

from app import app


@app.route('/')
@app.route('/index')
def index():
    return render_template('index.html')

@app.route('/error')
def error():
    return render_template('error.html'),400

@app.errorhandler(404)
def page_not_found(e):
    return render_template("error.html"), 404



