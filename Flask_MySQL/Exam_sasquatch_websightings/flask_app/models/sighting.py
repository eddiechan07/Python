from flask_app.config.mysqlconnection import connect_to_mysql
from flask import flash
from flask_app.models import user

class Sighting:
    
    DB ='Sasquatch_Websightings'
    
    def __init__(self, data):
        self.id = data['id']
        self.location = data['location']
        self.date_of_sighting = data['date_of_sighting']
        self.number_of_sasquatch = data['number_of_sasquatch']
        self.what_happened = data['what_happened']
        self.created_at =data['created_at']
        self.updated_at = data['updated_at']
        
    
    @classmethod
    def get_all_sightings(cls):
        query = """SELECT *, users.first_name AS user_name FROM sightings
                JOIN users ON sightings.user_id = users.id
                ORDER BY sightings.created_at DESC;
                """
        results = connect_to_mysql(cls.DB).query_db(query)
        sightings =[]
        if not results:
            return []
        for row in results:
            sighting = cls(row) 
            sighting.user_name = row['user_name']
            sightings.append(sighting)
        return sightings
    
    @classmethod
    def save_new_sighting(cls,data):
        query = """INSERT INTO sightings (location, date_of_sighting, number_of_sasquatch, what_happened, user_id, created_at, updated_at )
                VALUES(%(location)s, %(date_of_sighting)s, %(number_of_sasquatch)s, %(what_happened)s, %(user_id)s, NOW(), NOW());"""
        results = connect_to_mysql(cls.DB).query_db(query,data)
        return results
    
    @classmethod
    def delete(cls, data):
        query = "DELETE FROM sightings WHERE id = %(id)s"
        results = connect_to_mysql(cls.DB).query_db(query, data)
        return results
    
    @classmethod
    def edit(cls,data):
        query = """UPDATE sightings
                SET location=%(location)s, date_of_sighting=%(date_of_sighting)s, number_of_sasquatch=%(number_of_sasquatch)s, 
                what_happened=%(what_happened)s, created_at= NOW(), updated_at = NOW()
                WHERE id=%(id)s;"""
        results = connect_to_mysql(cls.DB).query_db(query,data)
        return results
    
    @classmethod
    def view(cls,data):
        query = """SELECT *, users.first_name AS user_name FROM sightings
                JOIN users ON sightings.user_id = users.id
                WHERE sightings.id = %(id)s"""
        results = connect_to_mysql(cls.DB).query_db(query,data)
        if not results:
            return False
        for row in results:
            sighting = cls(row) 
            sighting.user_name = row['user_name']
        return sighting


    
    