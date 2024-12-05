from mysqlconnection import connect_to_mysql
class User:
    DB = 'users_CR'
    def __init__(self, data):
        self.id = data['id']
        self.first_name = data['first_name']
        self.last_name = data['last_name']
        self.email = data['email']
        self.created_at = data ['created_at']

    @classmethod
    def create(cls, data):
        query = """INSERT INTO users_CR (first_name, last_name, email, created_at)
                VALUES (%(first_name)s, %(last_name)s, %(email)s, %(created_at)s);"""
        result = connect_to_mysql(cls.DB).query_db(query, data)
        return result

    @classmethod
    def read_all(cls):
        query = "SELECT * FROM users_CR;"
        result = connect_to_mysql(cls.DB).query_db(query)
        users = []
        for user in result:
            users.append(cls(user))
        return users



