from flask_app.models.user import User
from flask_app import app
from flask import redirect, render_template, session, request, url_for

@app.route('/')
def index():
    if 'user_id' in session:
        redirect('/dashboard')
    return render_template("registration.html")
@app.route('/register', methods=['POST'])
def register():
    data = request.form
    if User.validate_registration(data):
        user_id=User.register(data)
        session['user_id'] = user_id
        return redirect('/dashboard')
    return redirect(url_for('index'))

@app.route('/login' , methods=['POST'])
def login():
    data = request.form
    if User.validate_login(data):
        user = User.get_by_email(data)
        session['user_id'] = user.id
        return redirect('/dashboard')
    return redirect(url_for('index'))   

@app.route('/logout')
def logout():
    session.clear()
    return redirect(url_for('index'))