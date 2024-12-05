from flask_app.config.mysqlconnection import connect_to_mysql
from flask import flash
import re

EMAIL_REGEX = re.compile(r'^[a-zA-Z0-9.+_-]+@[a-zA-Z0-9._-]+\.[a-zA-Z]+$')
PASSWORD_REGEX = re.compile(r'^(?=.*[A-Z])(?=.*\d)')



class User:
    
    DB = 'CodingDojoWall'
    
    def __init__(self,data):
        self.id = data['id']
        self.first_name = data['first_name']
        self.last_name = data['last_name']
        self.email = data['email']
        self.password = data['password']
        self.created_at = data['created_at']
        self.updated_at = data['updated_at']
    
    @classmethod
    def register(cls,data):
        query = """ INSERT INTO users (first_name, last_name, email, password, created_at, updated_at)
                VALUES (%(first_name)s, %(last_name)s, %(email)s, %(password)s, NOW(), NOW());"""
        results = connect_to_mysql(cls.DB).query_db(query, data)
        return results
    
    @classmethod
    def get_by_email(cls, data):
        query = "SELECT * FROM users WHERE email = %(email)s;"
        results = connect_to_mysql(cls.DB).query_db(query, data)
        if len(results)<1:
            return None
        return cls(results[0])
    
    @classmethod
    def get_by_id(cls, data):
        query = "SELECT * FROM users WHERE id = %(id)s"
        results = connect_to_mysql(cls.DB). query_db(query,data)
        return cls(results[0])
        
    
    

    
    @staticmethod
    def validate_user(form_data):
        
        is_valid = True
        if len (form_data['first_name'])<2:
            flash("First name must be at least 2 characters!", 'register')
            is_valid = False
        if len (form_data['last_name'])<2:
            flash("Last name must be at least 2 characters!", 'register')
            is_valid = False     
        if not EMAIL_REGEX.match(form_data['email']):
            flash("Invalid email address!", 'register')
            is_valid = False
        if form_data['password'] != form_data['confirm_password']:
            flash("Password doesn't match!", 'register')
            is_valid = False
        if not PASSWORD_REGEX.search(form_data['password']):
            flash("Password should have at least one number and one uppercase letter", 'register')
            is_valid = False
        if len(form_data['password'])<8:
            flash("Email must be at least 2 characters!", 'register')
            is_valid = False
        return is_valid
    
        
    