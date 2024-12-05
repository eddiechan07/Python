from flask_app.config.mysqlconnection import connect_to_mysql


class Book:

    DB = "books_schema"
    def __init__(self, data):
        self.id = data['id']
        self.title = data['title']
        self.num_of_pages = data['num_of_pages']
        self.created_time = data['created_at']
        self.updated_time = data['updated_at']
    
    @classmethod
    def create_book(cls,data):
        query = """INSERT INTO books (title, num_of_pages)
                    VALUES(%(title)s, %(num_of_pages)s);"""
        results = connect_to_mysql(cls.DB).query_db(query, data)
        return results

    @classmethod
    def get_all_books(cls):
        query = "SELECT * FROM books;"
        results = connect_to_mysql(cls.DB).query_db(query)
        books=[]
        for row in results:
            books.append(cls(row))
        return books
    
    @classmethod
    def get_all_books_by_user(cls, data):
        query ="""SELECT * FROM books 
                LEFT JOIN favorites ON favorites.book_id = books_id
                LEFT JOIN users ON favorites.user_id = users.id
                WHERE users.id = %(id)s"""
        results = connect_to_mysql(cls.DB).query_db(query, data)
        books=[]
        for row in results:
            book={
                'book_id': row['book_id'],
                'title': row['title'],
                'num_of_pages': row['num_of_pages'],
                'user': {
                    'user_id': row['user_id'],
                    'name': row['name']
                }
            }
            books.append(book)
        return books

    