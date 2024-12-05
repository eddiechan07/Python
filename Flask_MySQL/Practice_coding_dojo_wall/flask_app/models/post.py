from flask_app.config.mysqlconnection import connect_to_mysql
from flask import flash


class Post:
    
    DB = 'CodingDojoWall'

    def __init__(self, data):
        self.id = data['id']
        self.content = data['content']
        self.created_at = data['created_at']
        self.updated_at = data['updated_at']
        self.user_id = data['user_id']
        self.first_name = data['first_name']
    
    @classmethod
    def save_posts(cls,data):
        query = """INSERT INTO posts (content, user_id, created_at, updated_at)
                VALUES (%(content)s, %(user_id)s, NOW(), NOW());"""
        results = connect_to_mysql(cls.DB).query_db(query, data)
        return results
    
    @classmethod
    def get_all_posts(cls):
        query = """SELECT *, users.first_name FROM posts
                LEFT JOIN users ON posts.user_id = users.id;"""
        results = connect_to_mysql(cls.DB).query_db(query)
        posts =[]
        for row in results:
            posts.append(cls(row))
        return posts
    
    
    
    @classmethod
    def get_posts_by_user_id(cls,data):
        query = """SELECT * FROM posts
                LEFT JOIN users ON posts.user_id = users.id
                WHERE users.id = %(id)s;"""
        results = connect_to_mysql(cls.DB).query_db(query,data)

        if not results:
            return None  
    
        return cls(results[0]) 
        
        


