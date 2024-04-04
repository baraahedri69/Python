from flask import Flask, render_template, session, redirect, url_for, request

app = Flask(__name__)
app.secret_key = 'your_secret_key'

@app.route('/', methods=['GET', 'POST'])
def index():
    if request.method == 'POST':
        action = request.form.get('action')
        if action == 'increment':
            session['visits'] = session.get('visits', 0) + 1
        elif action == 'reset':
            session['visits'] = 1
        return redirect(url_for('index'))
    else:
        session['visits'] = session.get('visits', 0)
        return render_template('index.html', visits=session['visits'])

if __name__ == '__main__':
    app.run(debug=True)