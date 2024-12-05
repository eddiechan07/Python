from flask_app.config.mysqlconnection import connect_to_mysql


class User:

    DB = "books_schema"
    def __init__(self, data):
        self.id = data['id']
        self.name = data['name']
        self.created_time = data['created_at']
        self.updated_time = data['updated_at']

    
    @classmethod
    def create_user(cls, data):
        query = """INSERT INTO users (name)
                    VALUES (%(name)s);"""
        return connect_to_mysql(cls.DB).query_db(query, data)
        
    
    @classmethod
    def get_all_users(cls):
        query = "SELECT * FROM users;"
        results = connect_to_mysql(cls.DB).query_db(query)
        users=[]
        for row in results:
            users.append(cls(row))
        return users
    
    @classmethod
    def get_by_id(cls, user_id):
        query = "SELECT * FROM users WHERE id = %(user_id)s;"
        data = {'user_id': user_id}
        results = connect_to_mysql(cls.DB).query_db(query, data)
        return cls(results[0])