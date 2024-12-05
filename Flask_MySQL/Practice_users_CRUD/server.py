from flask import Flask, render_template, redirect, render_template, session, request
from users import User
from datetime import datetime
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
        'first_name': request.form.get('first_name'),
        'last_name': request.form.get('last_name'),
        'email': request.form.get('email'),
        'created_at': request.form.get('created_at')
    }
    if not User.validate_user_data(user_data):
        return redirect('/')
    user_id = User.create(user_data)
    return redirect(f'/user/{user_id}')

#route to display all users
@app.route('/display')
def display_all():
    all_users = User.read_all()
    return render_template('show.html', all_users = all_users)

#show link
@app.route('/user/<int:id>')
def show_user(id):
    individual_user = User.get_by_id(id)
    return render_template('show_user.html', individual_user = individual_user)

#edit link
@app.route('/user/<int:id>/edit')
def edit(id):
    individual_user = User.get_by_id(id)
    return render_template('edit.html', individual_user = individual_user)

@app.route('/user/<int:id>/edit', methods=['POST'])
def update(id):
    user_data= {
        'id': id,
        'first_name': request.form['first_name'],
        'last_name': request.form['last_name'],
        'email': request.form['email'],
        'updated_at': datetime.now()
    }
    User.update(user_data)
    return redirect(f'/user/{id}')

#delete link
@app.route('/user/<int:id>/delete')
def delete(id):
    User.delete(id)
    return redirect('/display')




if __name__ == "__main__":
    app.run(debug=True, host = "127.0.0.1", port=8000)