from werkzeug.security import generate_password_hash, check_password_hash
from flask_login import UserMixin
from flask_login import LoginManager
from utils.db import db

login = LoginManager()

#extructura de la base de datos
#tabla de login

class logindb(UserMixin,db.Model):
    
    __tablename__ = 'users'

    id= db.Column(db.Integer,primary_key=True)
    username = db.Column(db.String(100))
    email= db.Column(db.String(100),unique=True)
    password= db.Column(db.String(102), nullable=False)


#genera la contrasena

    def set_password(self,password):
        return generate_password_hash(password)

    def check_password(self,password_hash,password):
        return check_password_hash(password_hash,password) 
        
#carga el usuario

@login.user_loader
def load_user(id):
    return logindb.query.get(int(id))


#tabla de estudiantes usados en el crud
class student(db.Model):

    __tablename__ = 'student'
    id= db.Column(db.Integer,primary_key=True)
    nombre =db.Column(db.String(50))
    correo = db.Column(db.String(100))
    telefono = db.Column(db.Integer)
    fecha_de_cumpleanos =db.Column(db.Date())

    def __init__(self,nombre,correo,telefono,fecha_de_cumpleanos):
        self.nombre = nombre
        self.correo = correo
        self.telefono =telefono
        self.fecha_de_cumpleanos = fecha_de_cumpleanos
        





   