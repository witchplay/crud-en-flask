from ctypes import create_unicode_buffer
from pickle import TRUE
from flask import Flask 
from routes.login import user_login
from routes.error import error
from routes.crud import crud
from flask_sqlalchemy import SQLAlchemy


app = Flask(__name__)

app.secret_key = 'S==%TxpO@E3@zA'

app.register_blueprint(user_login)
app.register_blueprint(error)
app.register_blueprint(crud)


app.config['SQLALCHEMY_DATABASE_URI'] = 'mysql://root:poiuy0mn@localhost/crud'
app.config[' SQLALCHEMY_TRACK_MODIFICATIONS'] = False

SQLAlchemy(app)


