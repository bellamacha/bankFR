import mysql.connector

class Database:
    def __init__(self):
        self.conn = mysql.connector.connect(
            user='root',
            password='h!TE4&$Q',
            database='work'
        )
        self.cursor = self.conn.cursor()
        self.conn.commit()
