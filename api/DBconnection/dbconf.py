import psycopg2

class PostgresConnection(object):
    def __init__(self):      #initialization
        self.connection = psycopg2.connect(database="ecomdb",
                                           user = "postgres",
                                           password = "admin",
                                           host = "127.0.0.1",
                                           port = "5432")

    def getConnection(self):
        print("Connection to DB established!")
        return self.connection