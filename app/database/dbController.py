import psycopg2

from app import app


class DatabaseConnection:
    def __init__(self):
        if app.config['TESTING']:
            print("Testing")
            self.con = psycopg2.connect(database="testdb", user="postgres",
                                        password="admin", host="localhost",
                                        port="5432"
                                        )
        else:
            print("Development")
            self.con = psycopg2.connect(database="mydiary", user="postgres",
                                        password="admin", host="localhost",
                                        port="5432"
                                        )

        self.con.autocommit = True
        self.cursor = self.con.cursor()

    def get_connection(self):
        return self.con

    """ This constructor is for creating the tables """

    def create_tables(self):

        queries = (
            """
            CREATE TABLE IF NOT EXISTS users (
                user_id SERIAL PRIMARY KEY,
                username VARCHAR(25) NOT NULL UNIQUE,
                emailaddress VARCHAR(50) NOT NULL UNIQUE,
                password VARCHAR(25) NOT NULL
            );
            """,

            """
            CREATE TABLE IF NOT EXISTS entries (
                entry_id SERIAL PRIMARY KEY,
                day VARCHAR(50) NOT NULL,
                title VARCHAR(50) NOT NULL UNIQUE,
                content VARCHAR(100) NOT NULL
            )
            """
        )
        for query in queries:
            self.cursor.execute(query)


    def delete_tables(self):

        delete_queries = (
            """
            DROP TABLE IF EXISTS users CASCADE
            """,

            """
            DROP TABLE IF EXISTS entries CASCADE
            """
        )
        for query in delete_queries:
            self.cursor.execute(query)
