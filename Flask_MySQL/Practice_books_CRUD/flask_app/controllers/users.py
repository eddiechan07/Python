from flask_app import app
from flask import render_template, redirect, request
from flask_app.models.user import User
from flask_app.models.book import Book


@app.route('/users')
def get_all_users():
    all_users = User.get_all_users()
    return render_template('users.html', all_users = all_users)

@app.route('/users/create_user', methods=['POST'])
def create_user():
    User.create_user(request.form)
    return redirect('/users')

@app.route('/users/<int:user_id>')
def show_all_books_in_one_user(user_id):
    user = User.get_by_id(user_id)
    books = Book.get_all_books_by_user(user_id)

    return render_template('show_all_books_in_one_user.html', user= user, books = books)


