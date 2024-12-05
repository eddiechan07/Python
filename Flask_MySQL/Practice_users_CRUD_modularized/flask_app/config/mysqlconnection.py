import pymysql.cursors

class MySQLConnection:
    def __init__(self, db):
        # Initialize the connection with root user credentials
        self.connection = pymysql.connect(
            host='localhost',
            user='root',        # Use root as the user
            password='Shumin621226!',  # Replace with your actual root password
            db=db,
            charset='utf8mb4',
            cursorclass=pymysql.cursors.DictCursor,
            autocommit=False
        )

    def query_db(self, query: str, data: dict = None):
        with self.connection.cursor() as cursor:
            try:
                # Mogrify the query with data
                query = cursor.mogrify(query, data)
                print("Running Query:", query)

                # Execute the query
                cursor.execute(query)

                # Check query type and return appropriate results
                if query.lower().find("insert") >= 0:
                    self.connection.commit()
                    return cursor.lastrowid
                elif query.lower().find("select") >= 0:
                    result = cursor.fetchall()
                    return result
                else:
                    self.connection.commit()
            except Exception as e:
                print("Something went wrong", e)
                return False

    # Close the connection when done (manually)
    def close_connection(self):
        self.connection.close()

# Helper function to create a connection instance
def connect_to_mysql(db):
    return MySQLConnection(db)
