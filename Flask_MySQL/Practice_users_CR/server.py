from flask import Flask, render_template, redirect, render_template, session, request
from users import User
app = Flask(__name__)
app.secret_key = 'your secretkey'

#route to show the form
@app.route('/')
def form():
    return render_template('index.html')

#route to create new user
@app.route('/create', methods=['POST'])
def create():
    user_data= {
        'id': request.form.get('id'),
        'first_name': request.form.get('first_name'),
        'last_name': request.form.get('last_name'),
        'email': request.form.get('email'),
        'created_at': request.form.get('created_at')
    }
    User.create(user_data)
    return redirect('/display')

#route to display all users
@app.route('/display')
def display_all():
    all_users = User.read_all()
    return render_template('show.html', all_users = all_users)

if __name__ == "__main__":
    app.run(debug=True, host = "127.0.0.1", port=8000)