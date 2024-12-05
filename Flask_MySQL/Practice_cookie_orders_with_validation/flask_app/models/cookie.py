from flask_app.config.mysqlconnection import connect_to_mysql
from flask import flash

class Cookie:

    DB = "cookies"
    def __init__(self, data):
        self.id = data['id']
        self.customer_name = data['customer_name']
        self.cookie_type = data['cookie_type']
        self.num_of_boxes = data['num_of_boxes']
        self.created_time = data['created_at']
        self.updated_time = data['updated_at']

    @classmethod
    def add_new_cookie(cls, data):
        query = """INSERT INTO cookies (customer_name, cookie_type, num_of_boxes)
                VALUES (%(customer_name)s, %(cookie_type)s, %(num_of_boxes)s);"""
        results = connect_to_mysql(cls.DB).query_db(query, data)
        return results
    
    @classmethod
    def show_cookie_orders(cls):
        query = "SELECT * FROM cookies"
        results = connect_to_mysql(cls.DB).query_db(query)
        cookies=[]
        if results:  # Only iterate if results are not None or False
            for row in results:
                cookies.append(cls(row))
        return cookies
    @classmethod
    def edit_cookie(cls, data):
        query = """UPDATE cookies
                SET customer_name = %(customer_name)s, cookie_type = %(cookie_type)s, num_of_boxes = %(num_of_boxes)s
                WHERE id = %(id)s;"""
        results = connect_to_mysql(cls.DB).query_db(query, data)
        return results

    @classmethod
    def get_cookie_by_id(cls, id):
        query = "SELECT * FROM cookies WHERE id = %(id)s"
        data = { 'id': id}
        results = connect_to_mysql(cls.DB).query_db(query, data)
        return cls(results[0])
    
    @staticmethod
    def validate_data(cookie):
        is_valid =True
        if len(cookie['customer_name'])<2:
            flash("Name must be at least 2 characters")
            is_valid=False
        if len(cookie['cookie_type'])<2:
            flash("Cookie type must be at least 2 characters")
            is_valid=False
        if int(cookie['num_of_boxes'])<=0:
            flash("Name must be at positive number")
            is_valid=False
        return is_valid
        
        
    
