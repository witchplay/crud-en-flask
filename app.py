from ctypes import create_unicode_buffer
from pickle import TRUE
from flask import Flask, render_template,redirect
from routes.login import user_login
from routes.crud import crud
from flask_sqlalchemy import SQLAlchemy


app = Flask(__name__)

app.secret_key = 'S==%TxpO@E3@zA'

app.register_blueprint(user_login)
app.register_blueprint(crud)


app.config['SQLALCHEMY_DATABASE_URI'] = 'mysql://bitcode:poiuy0mn@bitcode.mysql.pythonanywhere-services.com/bitcode$crud'
app.config[' SQLALCHEMY_TRACK_MODIFICATIONS'] = False



SQLAlchemy(app)

@app.errorhandler(404)
def page_not_found(error):
    return render_template('404.html'), 404


