from crypt import methods
import imp
from flask import Blueprint,render_template,redirect,url_for,request,flash
from flask_login import login_required
from models.models import student
from utils.db import db


crud = Blueprint('crud',__name__)

#ruta del crud
@crud.route('/crud')
@login_required
def home_crud():
    students = student.query.all()
    return render_template('crud.html',students = students)

#ruta de add
@crud.route('/add', methods=['POST','GET'])
@login_required
def add():


    if request.method == 'POST':
       nombre = request.form['nombre']
       correo = request.form['correo']
       telefono = request.form['telefono']
       fecha_de_cumpleanos = request.form['fecha']
       students= student(nombre=nombre,correo=correo,telefono=telefono,fecha_de_cumpleanos=fecha_de_cumpleanos)
       db.session.add(students)
       db.session.commit()

       flash('Agregado correctamente')

       return redirect(url_for('crud.home_crud'))
    else:

        return render_template('add.html')

#ruta de update
@crud.route('/update/<id>', methods=['POST','GET'])
@login_required
def update(id):
    updateid = student.query.get(id)

    if request.method == 'POST':
       updateid.nombre = request.form['nombre']
       updateid.correo = request.form['correo']
       updateid.telefono = request.form['telefono']
       updateid.fecha_de_cumpleanos = request.form['fecha']
       db.session.commit()

       flash('Modificado correctamente')

       return redirect(url_for('crud.home_crud'))
    else:

        return render_template('update.html',updateid = updateid)

#ruta de delete
@crud.route('/delete/<id>')
@login_required
def delete(id):
    deleteid =  student.query.get(id)
    db.session.delete(deleteid)
    db.session.commit()
    flash('Borrado correctamente')
    return redirect(url_for('crud.home_crud'))



#ruta de about
@crud.route('/about')
@login_required
def about():
   return render_template('about.html')



