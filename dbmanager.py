import psycopg2 as p6
class dbmanager :
    def __init__(self):
        self.conn = p6.connect(database= "hello",user= "postgres",password = "secret",host= "localhost",port = 5432)
        self.curr = self.conn.cursor()

    