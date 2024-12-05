from flask_app import app
from flask import render_template, request, redirect, session, flash
from flask_app.models.user import User 
from flask_bcrypt import Bcrypt
bcrypt = Bcrypt(app)


@app.route('/')
def register_and_login():
    return render_template('index.html')

@app.route('/register', methods=['POST'])
def register():
    if not User.validate_user(request.form):
        return redirect('/')

    pw_hash = bcrypt.generate_password_hash (request.form['password'])
    data ={
        'first_name' : request.form['first_name'],
        'last_name' : request.form['last_name'],
        'email' : request.form['email'],
        'password' : pw_hash
    }

    user = User.save(data)
    session['user_id'] = user.id
    return redirect('/dashboard')

@app.route('/login', methods=['POST'])
def login():
    data = {"email" : request.form['email']}
    user = User.get_by_email(data)
    if not user:
        flash("Invalid Email/Password", 'login')
        return redirect('/')
    if not bcrypt.check_password_hash(user.password, request.form['password']):
        flash("Invalid Email/Password", 'login')
        return redirect('/')
    session['user_id'] = user.id
    return redirect('/dashboard')

@app.route('/dashboard')
def dashboard():

    if 'user_id' not in session:
        return redirect('/')

    user_id = session['user_id']

    user = User.get_by_id({'id': user_id})
    if not user:
       return redirect('/')

    return render_template('dashboard.html', user= user)

@app.route('/logout', methods=['POST'])
def log_out():
    session.clear()
    return redirect('/')



