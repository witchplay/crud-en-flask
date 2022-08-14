from flask_wtf import FlaskForm
from wtforms import StringField, SubmitField, PasswordField,IntegerField, validators
from wtforms.fields.html5 import DateField
from wtforms.validators import DataRequired, Email, Length

class SignupForm(FlaskForm):
    username = StringField('nombre', validators = [DataRequired(message="El campo debe tener minimo 3 caracteres"), Length(min = 3,max = 50)],render_kw={"placeholder": "Nombre de usuario"})
    password = PasswordField('password',[ validators.DataRequired(message='la contrasena de tener 5 caracteres'), validators.EqualTo('confirm', message='Las contraseñas deben coincidir'),Length(min =5)],render_kw={"placeholder": "Contraseña"})
    confirm = PasswordField('Repeat Password',render_kw={"placeholder": "Repite la contraseña"})
    email = StringField('email', validators=[DataRequired(), Email(),Length(max=128)],render_kw={"placeholder": "Correo","type":"email"})
    submit = SubmitField('Registrar')

class LoginForm(FlaskForm):
    email = StringField('email', validators = [DataRequired(message= 'El corrreo debe tener %(min) caracteres'), Email(granular_message=True), Length(min= 3,max=128) ],render_kw={"placeholder": "Email","type":"email"})
    password = PasswordField('password',[validators.DataRequired()],render_kw={"placeholder": "Contraseña"})
    submit = SubmitField('Iniciar sesión')


class AddForm(FlaskForm):
    nombre = StringField('nombre',validators = [DataRequired(),Length(min = 3,max = 50 , message = "El campo debe tener minimo 3 caracteres ")],render_kw={"placeholder": "Nombre"})
    correo =  StringField('correo', validators = [DataRequired(message= 'El corrreo debe tener %(min) caracteres'), Email(granular_message=True), Length(min = 3,max=128,message= 'El corrreo debe tener %(min) caracteres') ],render_kw={"placeholder": "Correo","type":"email"})
    telefono = IntegerField('telefono', [DataRequired(message="Introduce el numero de telefono")],render_kw={"placeholder": "Telefono"})
    fecha = DateField(validators = [DataRequired(message= 'Debes ingresar una fecha')])
    submit = SubmitField('Agregar')



class UpdateForm(FlaskForm):
    nombre = StringField('nombre',validators = [DataRequired(),Length(min = 3, max = 50,message="El campo debe tener minimo 3 caracteres")],render_kw={"placeholder": "Nombre"})
    correo =  StringField('correo', validators = [DataRequired(message= 'El corrreo debe tener %(min) caracteres'), Email(granular_message=True), Length(min=3,max=128,message= 'El corrreo debe tener %(min) caracteres') ],render_kw={"placeholder": "Correo","type":"email"})
    telefono = IntegerField('telefono', [DataRequired(message="Introduce el numero de telefono")],render_kw={"placeholder": "Telefono"})
    fecha = DateField(validators = [DataRequired(message= 'Debes ingresar una fecha')])
    submit = SubmitField('Actualizar')

