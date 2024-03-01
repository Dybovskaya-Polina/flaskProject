from flask import render_template

from app import app


@app.route('/')
@app.route('/index')
def f():
    return render_template('2.html')

@app.route('/error')
def r():
    return render_template('error.html'),400

@app.errorhandler(404)
def page_not_found(e):
    return render_template("error.html"), 404


