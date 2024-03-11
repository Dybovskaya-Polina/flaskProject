from flask import render_template, session, redirect, url_for
from app.forms import ContactForm
from app import app


@app.route('/')
@app.route('/index')
def index():
    def_user = 'friend'
    session_info = session.get('name')
    if session_info is None:
        return render_template('index.html', name=def_user)
    else:
        return render_template('index.html', name=session_info)

@app.route('/error')
def error():
    return render_template('error.html'), 403


@app.errorhandler(404)
def page_not_found(e):
    return render_template("error.html"), 404



@app.route('/form', methods=['GET','POST'])
def testForm():
    name = None
    form = ContactForm()
    if form.validate_on_submit():
        session['name'] = form.name.data
        form.name.data = ''
        return redirect(url_for('index'))
    return render_template('form.html', form=form, name=name)