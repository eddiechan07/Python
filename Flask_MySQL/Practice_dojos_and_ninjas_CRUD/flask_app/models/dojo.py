from flask_app.config.mysqlconnection import connect_to_mysql



class Dojo:

    DB = "dojos_and_ninjas_schema_CRUD"
    def __init__(self,data):
        self.id = data['id']
        self.cities = data['cities']
        self.created_time = data['created_at']
        self.updated_time = data['updated_at']
    
    @classmethod
    def create_dojo(cls, data):
        query = """INSERT INTO dojos(cities)
                VALUES(%(cities)s);"""
        return connect_to_mysql(cls.DB).query_db(query,data)
    
    @classmethod
    def get_all_dojos(cls):
        query = "SELECT * FROM dojos;"
        results = connect_to_mysql(cls.DB).query_db(query)
        dojos =[]
        for row in results:
            dojos.append(cls(row))
        return dojos

    @classmethod
    def get_by_id(cls, dojo_id):
        query = "SELECT * FROM dojos WHERE id = %(id)s;"
        data = {"id":dojo_id}
        print(f"Running query: {query} with data: {data}")
        results = connect_to_mysql(cls.DB).query_db(query, data)
        print(f"Results for dojo query: {results}")
        return cls(results[0]) if results else None


