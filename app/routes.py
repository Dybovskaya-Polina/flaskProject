
from flask import render_template, session, redirect, url_for, request
from werkzeug.security import generate_password_hash
from models import Users,Profiles
from app.forms import ContactForm
from app import app, db


@app.route('/')
@app.route('/index')
def index():
    info = []
    try:
        info = Users.query.all()
    except:
        print("Ошибка чтения из БД")
    return render_template('index.html',list=info)



@app.route('/register', methods=['POST','GET'])
def register():
    if request.method == 'POST':
        try:
            hash = generate_password_hash(request.form['psw'])
            u = Users(email=request.form['email'], psw=hash)
            print(u,hash)
            db.session.add(u)
            db.sessiion.flush()
            p = Profiles(name=request.form['name'], city=request.form['city'], user_id=u.id)
            db.session.add(p)
            db.session.commit()
        except:
            db.session.rollback()
            print('error in db')
        return redirect(url_for('index'))

    return render_template('form2.html')


'''
@app.route('/form', methods=['GET', 'POST'])
def testForm():
    name = None
    form = ContactForm()
    if form.validate_on_submit():
        session['name'] = form.name.data
        form.name.data = ''
        return redirect(url_for('index'))
    return render_template('form.html', form=form, name=name)
'''
@app.route('/error')
def error():
    return render_template('error.html'), 403


@app.errorhandler(404)
def page_not_found(e):
    return render_template("error.html"), 404

