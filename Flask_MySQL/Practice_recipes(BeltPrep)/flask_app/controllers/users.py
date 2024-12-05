from flask_app import app
from flask import render_template, request, session, redirect, flash
from flask_app.models import user
from flask_app.models import recipe
from flask_bcrypt import Bcrypt

bcrypt = Bcrypt(app)

@app.route('/')
def register_and_login():
    return render_template('index.html')

@app.route('/register', methods=['POST'])
def register():                                                        # Register
    if not user.User.validate_user(request.form):                      # 1st: check user's input follows the rules (.validate_user() method)
        return redirect('/')
    
    pw_hash = bcrypt.generate_password_hash(request.form['password'])  # 2nd: if user's input valid, hash the password (.generate_password_hash() method)
    data ={                                                            # 3rd: create user's data dictionary, with hashed password
        'first_name' : request.form['first_name'],
        'last_name' : request.form['last_name'],
        'email' : request.form['email'],
        'password' : pw_hash
    }
    user_id = user.User.register(data)                                 # 4th: pass user's data into database (.register()/save() method)
    
    if not user_id:                                                    # 5th: if failed to insert a new user into the database, redirect
        return redirect('/')

    session['user_id'] = user_id                                       # 6th: otherwise, save user's ID into the session, and redirect
    return redirect('/')

@app.route('/login', methods=['POST'])                                 
def login():                                                           # Login
    data = {"email": request.form["email"]}
    user_in_db = user.User.get_by_email(data)                          # 1st: pass user's email input into database (.get_by_email() method)
    if not user_in_db:                                                 # 2nd: if user is not found in the database, redirect
        flash("Invalid Email", 'login')
        return redirect('/')
    if not bcrypt.check_password_hash(user_in_db.password, request.form['password']): # 3rd: if user's data of password is different from input, redirect
        flash("Invalid Password", 'login')
        return redirect('/')
    session['user_id'] = user_in_db.id                                 # 4h: otherwise, save user's id into the session, and redirect
    return redirect('/recipes')

@app.route('/logout')
def logout():
    session.clear()
    return redirect('/')
        

    


