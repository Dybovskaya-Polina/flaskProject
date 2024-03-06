from flask import render_template, session, redirect, url_for
from app.forms import ContactForm
from app import app


@app.route('/')
@app.route('/index')
def index():
    def_user = 'friend'
    session_info = session.get('text')
    if session_info is None:
        return render_template('index.html', text=def_user)
    else:
        return render_template('index.html', text=session_info)


@app.route('/error')
def error():
    return render_template('error.html'), 403


@app.errorhandler(404)
def page_not_found(e):
    return render_template("error.html"), 404


@app.route('/form', methods=['GET','POST'])
def forma():
    text = None
    form = ContactForm()
    '''
    if form.validate_on_submit():
        session['text'] = form.text.data
        form.text.data = ''
        return redirect(url_for('index'))
        '''
    return render_template('form.html', form=form, text=text)
