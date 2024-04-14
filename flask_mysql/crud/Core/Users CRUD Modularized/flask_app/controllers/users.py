from flask import render_template, redirect, request
from flask_app import app
from flask_app.models.user import User

#  VIEW ALL USERS
@app.route('/')
def index():
    return redirect('/users')

@app.route('/users')
def users():
    context = {
        'users' : User.get_all()
    }
    return render_template("read_all.html", **context)
# @app.route('/users', methods=['GET'])
# def users():
    # """View all users."""
    # user = User()
    # data = user.getAllUsers()
    # return render_template('admin/users.html', title='Usuarios', data=data)
# ADD NEW USER

@app.route('/users/new')
def new():
    return render_template("create.html")

@app.route('/users/create',methods=['POST'])
def create():
    User.save(request.form)
    return redirect('/users')
# @app.route('/add-new-user', methods=['POST'])
# def addNewUser():
#     """Add new user."""
#     name = request.form.get("name")
#     email = request.form.get("email")
#     password = request.form.get("password")
#     role = request.form.get("role")
#     if not (name and email):
#         return "Faltan campos por llenar"
#     else:
#         user = User(name, email, password, role)
#         result = user.insertUser()
#         if result == True:
#             return 'Se ha agregado el usuario correctamente'
#         elif result == False:
#             return 'No se pudo agregar el usuario'
#         else:
#             return str(result)
        

# UPDATE USER

@app.route('/user/edit/<int:id>')
def edit(id):
    data ={
        "id":id
    }
    context = {
        'user' : User.get_one(data)
    }
    return render_template("edit.html", **context)

@app.route('/user/update', methods=['POST'])
def update():
    User.update(request.form)
    return redirect('/users')


# SHOW ONE USER
@app.route('/user/show/<int:id>')
def show(id):
    data ={
        "id":id
    }
    context = {
        'user' : User.get_one(data)
    }
    return render_template('read_one.html',**context)

# DELETE USER
@app.route('/user/delete/<int:id>')
def delete(id):
    data = {
        'id':id
    }
    User.delete(data)
    return redirect('/users')
