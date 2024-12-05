from flask_app.config.mysqlconnection import connect_to_mysql

class Ninja:

    DB = "dojos_and_ninjas_schema_CRUD"
    def __init__(self,data):
        self.id = data['id']
        self.first_name = data['first_name']
        self.last_name = data['last_name']
        self.age = data['age']
        self.created_time = data['created_at']
        self.updated_time = data['updated_at']
    
    @classmethod
    def create_ninja(cls, data):
        query = """INSERT INTO ninjas(dojos_id, first_name, last_name, age)
                VALUES(%(dojos_id)s, %(first_name)s, %(last_name)s, %(age)s);"""
        return connect_to_mysql(cls.DB).query_db(query,data)
    
    @classmethod
    def get_all_by_dojo(cls, dojo_id):
        query = "SELECT * FROM ninjas WHERE dojos_id = %(dojos_id)s"
        data = {"dojos_id" : dojo_id}
        print(f"Running query: {query} with data: {data}")
        results = connect_to_mysql(cls.DB).query_db(query,data)
        print(f"Results for ninjas query: {results}")
        if not results:
            return []
        ninjas = []
        for row in results:
            ninjas.append(cls(row))
        return ninjas