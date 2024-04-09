from flask import Flask, render_template, request, redirect
from flask_mysqldb import MySQL

app = Flask(__name__)
app.config['MYSQL_HOST'] = 'localhost'
app.config['MYSQL_USER'] = 'root'
app.config['MYSQL_PASSWORD'] = 'shax12345678'
app.config['MYSQL_DB'] = 'users'  
app.config['MYSQL_CURSORCLASS'] = 'DictCursor'

mysql = MySQL(app)

@app.route('/')
def read_all():
    from users import Users 
    users = Users.get_all_users()
    return render_template('read_all.html', users=users)

@app.route('/create', methods=['GET', 'POST'])
def create():
    from users import Users 
    if request.method == 'POST':
        first_name = request.form['first_name']
        last_name = request.form['last_name']
        email = request.form['email']
        Users.create_user(first_name, last_name, email)
        return redirect('/')
    return render_template('create.html')

if __name__ == '__main__':
    app.run(debug=True)