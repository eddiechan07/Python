from flask_app import app
from flask import render_template, redirect, request
from flask_app.models.book import Book



@app.route('/books')
def get_all_books():
    all_books = Book.get_all_books()
    return render_template('books.html', all_books = all_books)

@app.route('/books/create_book', methods=['POST'])
def create_book():
    if 'title' not in request.form or 'num_of_pages' not in request.form:
        return "Missing form data", 400

    data = {
        'title' : request.form['title'],
        'num_of_pages' : request.form['num_of_pages']
    }   
    Book.create_book(data)
    return redirect('/books')

