from flask import Flask,render_template,request,session,redirect

import api
from db import Database
from api im


app = Flask(__name__)
dbo = Database()


@app.route('/')
def index():
    return render_template('login.html')


@app.route('/register')
def register():
    return render_template('register.html')


@app.route('/perform_registration',methods=['post'])
def perform_registration():
    name = request.form.get('user_name')
    email = request.form.get('email')
    password = request.form.get('password')

    responce = dbo.insert(name,email,password)

    if responce:
        return render_template('login.html', message= 'Registration Successful. Kindly login to proceed')
    else:
        return render_template('login.html', message= 'Email already exist.')


@app.route('/perform_login', methods = ['post'])
def perform_login():
    email = request.form.get('user_email')
    password = request.form.get('password')

    res = dbo.search(email,password)

    if res:
        session['logged_in']  = 1
        return redirect('/profile.html')
    else:
        return render_template('login.html', message = 'Incorrect Email/Password')


@app.route('/profile')
def profile():
    if session['logged_in'] == 1:
     return render_template('profile.html')
    else:
        redirect('/')

@app.route('/NER')
def NER():
    if session['logged_in'] == 1:
        return render_template('ner.html')
    else:
        return redirect('/')


@app.route('/perform_ner',methods= ['post'])
def perform_ner():
    if session['logged_in'] == 1:
        text = request.form.get('ner_text')
        responce = api.ner(text)

        ans = ' '
        for i in responce['entities']:
            ans = ans +i['category']+' :- '+i['name'] + '   '+'\n'
        return ans
    else:
        return redirect('/')
app.run(debug=True)
