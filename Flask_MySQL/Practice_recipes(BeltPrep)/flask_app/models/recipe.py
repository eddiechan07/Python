from flask_app.config.mysqlconnection import connect_to_mysql
from flask import flash

class Recipe:
    
    DB = 'recipes'

    def __init__(self, data):
        self.id = data['id']
        self.name = data['name']
        self.description = data['description']
        self.instructions = data['instructions']
        self.date_cooked = data['date_cooked']
        self.under_30_minutes = data['under_30_minutes']
        self.created_at = data['created_at']
        self.updated_at = data['updated_at']
        
    @classmethod
    def add_new_recipe(cls, data):
        query = """INSERT INTO recipes (name, description, instructions, date_cooked, under_30_minutes, user_id)
                VALUES (%(name)s, %(description)s, %(instructions)s, %(date_cooked)s, %(under_30_minutes)s, %(user_id)s);"""
        results = connect_to_mysql(cls.DB).query_db(query, data)
        return results   
    @classmethod
    def get_all_recipes(cls):
        query = """SELECT * FROM recipes
                LEFT JOIN users ON recipes.user_id = users.id"""
        results = connect_to_mysql(cls.DB).query_db(query)
        recipes =[]
        for row in results:
            recipe_instance = cls(row)
            recipe_instance.creator = f"{row['first_name']}"
            recipes.append(recipe_instance)
        return recipes
    @classmethod
    def get_one_recipe(cls, data):
        query = "SELECT * FROM recipes WHERE id = %(id)s;"
        results = connect_to_mysql(cls.DB).query_db(query,data)
        return cls(results[0])
    @classmethod
    def delete(cls, data):
        query = "DELETE  FROM recipes WHERE id = %(id)s"
        results = connect_to_mysql(cls.DB).query_db(query, data)
        return results
    @classmethod
    def update(cls,data):
        query = """UPDATES recipes 
                SET name = %(name)s, description = %(description)s, instructions = %(instructions)s, date_cooked = %(date_cooked)s, under_30_minutes = %(under_30_minutes)s
                WHERE id = %(id)s"""
        results = connect_to_mysql(cls.DB).query_db(query, data)
        return results
    
    @staticmethod
    def validate_recipe(form_data):
        is_valid=True
        if len(form_data['name'])<2:
            flash("Name must be at least 3 characters")
            is_valid=False
        if len(form_data['description'])<2:
            flash("Name must be at least 3 characters")
            is_valid=False
        if len(form_data['instructions'])<2:
            flash("Name must be at least 3 characters")
            is_valid=False
        return is_valid
        
    
    
    