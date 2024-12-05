from flask_app import app
from flask import render_template, redirect, request, session, flash
from flask_app.models import user
from flask_bcrypt import Bcrypt

bcrypt = Bcrypt(app)


@app.route('/')
def register_and_login():
    return render_template('index.html')

@app.route('/register', methods=['POST'])
def register():
    if not user.User.validate_user(request.form):
        return redirect('/')
    
    pw_hash = bcrypt.generate_password_hash(request.form['password'])
    
    data ={
        'first_name' : request.form['first_name'], 
        'last_name' : request.form['last_name'], 
        'email' : request.form['email'], 
        'password' : pw_hash 
    }
    
    user_id = user.User.register(data)
    if not user_id:
        return redirect('/')
    session['user_id'] = user_id
    
    return redirect('/')

@app.route('/login', methods=['POST'])
def login():
    data = {'email' : request.form['email']}
    user_in_db = user.User.get_by_email(data)
    if not user_in_db:
        flash("Invalid email address", 'login')
        return redirect('/')
    if not bcrypt.check_password_hash(user_in_db.password, request.form['password']):
        flash("Invalid password", 'login')
        return redirect('/')
    
    session['user_id'] = user_in_db.id
    return redirect('/wall')

@app.route('/logout')
def logout():
    session.clear()
    flash('You have successfully logged out', 'logout')
    return redirect('/')




