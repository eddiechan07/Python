from flask_app.config.mysqlconnection import connect_to_mysql
from flask import flash
import re 

EMAIL_REGEX = re.compile(r'^[a-zA-Z0-9.+_-]+@[a-zA-Z0-9._-]+\.[a-zA-Z]+$')
PASSWORD_REGEX = re.compile(r'^(?=.*[A-Z])(?=.*\d)')

class User:
    
    DB = "my_login_and_registration_db"

    def __init__(self, data):
        self.id = data['id']
        self.first_name = data['first_name']
        self.last_name = data['last_name']
        self.email = data['email']
        self.password = data['password']
        self.confirm_password = data['password']
        self.created_at = data['created_at']
        self.updated_time = data['updated_at']
    
    @classmethod
    def save(cls, data):
        query = """INSERT INTO users (first_name, last_name, email, password)
                VALUES (%(first_name)s, %(last_name)s, %(email)s, %(password)s);"""
        return connect_to_mysql(cls.DB).query_db(query, data)

    @classmethod
    def get_by_email(cls, data):
        query = "SELECT * FROM users WHERE email = %(email)s;"
        results = connect_to_mysql(cls.DB).query_db(query, data)
        if len(results)<1:
            return False
        return cls(results[0])
    
    @classmethod
    def get_by_id(cls, data):
        query = "SELECT * FROM users WHERE id = %(id)s"
        results = connect_to_mysql(cls.DB).query_db(query, data)
        return cls(results[0])


    @staticmethod
    def validate_user(user):
        is_valid = True
        if len(user['first_name'])<2:
            flash("First Name should be at least 2 characters.", 'register')
            is_valid = False
        if len(user['last_name'])<2:
            flash("Last Name should be at least 2 characters.", 'register')
            is_valid = False
        if len(user['password'])<8:
            flash("Password should be at least 8 characters.", 'register')
            is_valid = False
        if not EMAIL_REGEX.match(user['email']):
            flash("Invalid email.", 'register')
            is_valid = False
        if not PASSWORD_REGEX.search(user['password']):
            flash("Password should have at least one number and one uppercase letter.", 'register')
            is_valid = False
        if user['password'] != (user['confirm_password']):
            flash("Password doesn't match", 'register')
            is_valid = False
        return is_valid
    

