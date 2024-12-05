from flask_app.config.mysqlconnection import connect_to_mysql
from flask import flash
import re

EMAIL_REGEX = re.compile(r'^[a-zA-Z0-9.+_-]+@[a-zA-Z0-9._-]+\.[a-zA-Z]+$')
PASSWORD_REGEX = re.compile(r'^(?=.*[A-Z])(?=.*\d)')


class User:
    
    DB = 'recipes'
    
    def __init__(self, data):
        self.id = data['id']
        self.first_name = data['first_name']
        self.last_name = data['last_name']
        self.email = data['email']
        self.password = data['password']
        self.created_at = data['created_at']
        self.updated_at = data['updated_at']
    
    
    @classmethod
    def register(cls, data):                                                                             # Create: register(cls, data) / save(cls, data)
        query = """INSERT INTO users (first_name, last_name, email, password, created_at, updated_at)
                    VALUES(%(first_name)s, %(last_name)s, %(email)s, %(password)s, NOW(), NOW());"""
        results = connect_to_mysql(cls.DB).query_db(query, data)
        return results
    @classmethod
    def get_by_email(cls, data):                                                                         # Read(1): get_by_one(cls, data)
        query = "SELECT * FROM users WHERE email = %(email)s;"
        results = connect_to_mysql(cls.DB).query_db(query, data)
        if not results:                                                                                   # if no matched dictionary
            return False
        return cls(results[0])                                                                            # otherwise, return that email
    @classmethod
    def get_all_user(cls):                                                                                     # Read(2): get_all(cls)
        query = "SELECT * FROM users"
        results = connect_to_mysql(cls.DB).query_db(query)
        users = []
        for user in results:
            users.append(cls(user))                                                                       # put all into a new list
        return users
    @classmethod
    def get_by_id(cls, data):
        query = "SELECT * FROM users WHERE id = %(id)s"
        results = connect_to_mysql(cls.DB).query_db(query, data)
        if not results:                                                                                   
            return False
        return cls(results[0])  
    # @classmethod
    # def get_recipes_by_id(cls, id):
    #     query = """SELECT * FROM user 
    #             LEFT JOIN recipes ON recipes.user_id = users.id
    #             WHERE id = %(id)s"""
    #     data = {'id' : id}
    #     results = connect_to_mysql(cls.DB).query_db(query, data)
        
    
    
    
    @staticmethod
    def validate_user(form_data):                                                                         # Set up the flash (.validate_user() method)
        is_valid = True
        if len(form_data['first_name'])<2:
            flash("First Name must be at least two characters!", 'register')                              # set up flash category
            is_valid=False
        if len(form_data['last_name'])<2:
            flash("Last Name must be at least two characters!", 'register')
            is_valid=False
        if not EMAIL_REGEX.match(form_data['email']):
            flash("Invalid email address", 'register')    
            is_valid=False
        if (form_data['password']) != (form_data['confirm_password']):
            flash("Password doesn't match!", 'register')
            is_valid=False
        
        # if len(form_data['password'])<8:
        #     flash("Password should be at least 8 characters.")
        #     is_valid = False
        # if not PASSWORD_REGEX.search(user['password']):
        #     flash("Password should have at least one number and one uppercase letter.!")
        #     is_valid=False
        return is_valid