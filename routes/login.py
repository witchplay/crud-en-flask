from werkzeug.security import generate_password_hash
from crypt import methods
from click import password_option
from flask import Blueprint,render_template,request,redirect, url_for,flash
from models.models import logindb
from flask_login import current_user, login_required, login_user, logout_user
from utils.db import db

user_login = Blueprint('user_login', __name__)

#ruta raiz
@user_login.route('/')
def index ():
    return redirect('login')

#ruta login
@user_login.route('/login',methods=['GET','POST'])
def login():
    sing_up= 'sing_up'
    if current_user.is_authenticated:
        return redirect('/crud')
    
    if request.method == "POST":
         email = request.form['email']
         user = logindb.query.filter_by(email = email).first()
         if user is not None and user.check_password(user.password,request.form['password']):
             login_user(user)
             return redirect('/crud')
         
    return render_template('login.html', sing_up = sing_up)

#ruta register
@user_login.route('/register', methods = ['GET','POST'])
def register():
    sing_up = 'Iniciar Sesión'

    if current_user.is_authenticated:
        return redirect('/')

    if request.method == 'POST':
        username = request.form['username']
        email = request.form['email']
        password = request.form['password']
        print(password)

        if logindb.query.filter_by(email=email).first():
            flash('Correo ya existente')
            return redirect('/register')

        hash = generate_password_hash(password)
        user = logindb(username=username,email=email,password=hash)
        db.session.add(user)
        db.session.commit()

        return redirect('/login')
        
    return render_template('register.html',sing_up = sing_up)

#ruta de logout
@user_login.route('/logout')
def logout():
    logout_user()
    return redirect(url_for('user_login.login'))
