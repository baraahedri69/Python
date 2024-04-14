from flask_app import app
from flask import render_template,redirect,request
from flask_app.models import ninja, dojo


@app.route('/ninjas')
def ninjas():
    context = {
        'dojos' : dojo.Dojo.get_all()
    }
    return render_template("add_ninja.html", **context)

@app.route('/ninjas/add',methods=['POST'])
def create_ninja():
    ninja.Ninja.save(request.form)
    return redirect('/')
