import sqlite3

class Database:
    def __init__(self):
        self.conn = sqlite3.connect('data.db',check_same_thread=False)
        self.cur = self.conn.cursor()
        self.DropTable()
        self.createTable()

    def createTable(self):
        self.cur.execute('''
            CREATE TABLE person(
                id INTEGER PRIMARY KEY AUTOINCREMENT,
                name varchar(60) NOT NULL,
                latitude varchar(255) NOT NULL,
                longitude varchar(255) NOT NULL,
                timestamp DATETIME DEFAULT(datetime(CURRENT_TIMESTAMP,'localtime'))
            );''')

    def DropTable(self):
        self.cur.execute('''DROP TABLE IF EXISTS person;''')
    
    def insertData(self,name,latitude,longitude):
        self.cur.execute('''
            INSERT INTO person (name,latitude,longitude)
            VALUES ('{}','{}','{}')
        '''.format(name,latitude,longitude)
        )
        
        self.commit()

    def SelectAll(self):
        self.cur.execute('''SELECT * FROM person''') 
        db = self.cur.fetchall()
        return db

    def commit(self):
        self.conn.commit()
