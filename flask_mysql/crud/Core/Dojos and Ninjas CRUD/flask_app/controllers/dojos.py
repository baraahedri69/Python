from flask_app import app
from flask import render_template,redirect,request
from flask_app.models.dojo import Dojo
# from flask_app.models.ninja import Ninja

@app.route('/')
def index():
    return redirect('/dojos')


@app.route('/dojos')
def dojos():
    context ={
        'dojos' : Dojo.get_all()
    }
    return render_template('dojo.html',**context)

@app.route('/dojos/create',methods=['POST'])
def create():
        Dojo.save(request.form)
        return redirect('/dojos')


@app.route('/dojo/<int:id>')
def show(id):
    data ={
        "id":id
    }
    context = {
        'dojos' : Dojo.get_alldojo_with_members(data)
    }
    return render_template("dojo_members.html", **context)
