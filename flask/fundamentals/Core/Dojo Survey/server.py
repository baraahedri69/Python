from flask import Flask, render_template, request, session, redirect

app = Flask(__name__)
app.secret_key = 'Ouch'

@app.route('/')
def index():
    return render_template("index.html")

@app.route('/process',methods=['POST'])
def process(): 
        session['name'] = request.form['name']
        session['location'] = request.form['location']
        session['language'] = request.form['language']
        session['comment'] = request.form['comment']
        return redirect('/result')

@app.route('/result')
def result():
    name = session.get('name')
    location = session.get('location')
    language = session.get('language')
    comment = session.get('comment')
    return render_template('result.html',name=name, location=location, language=language, comment=comment)

if __name__ == '__main__':
    app.run(debug=True)