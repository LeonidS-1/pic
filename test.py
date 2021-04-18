import sqlite3
from random import randint


class DataBase:
    def __init__(self, name):
        self.con = sqlite3.connect(name)
        self.cur = self.con.cursor()
        self.create_table()
    
    def create_table(self, name_table='score'):
        que_create_table = f'''
        CREATE TABLE IF NOT EXISTS {name_table} (
            id INTEGER PRIMARY KEY,
            name TEXT
            points INTEGER
        )'''
        self.cur.execute(que_create_table)
        self.con.commit()

    def get(self, que='SELECT * FROM score ORDER BY points DESC'):
        return self.cur.execute(que).fetchall()

    def insert(self, name, points):
        que_insert = f'''
        INSERT INTO score (name, points) VALUES
            ('{name}', {points})
        '''
        self.cur.execute(que_insert)
        self.con.commit()
    
    def __del__(self):
        self.con.close()


db = DataBase('test.sqlite3')

# data_from_db = db.get()
# print(*data_from_db, sep='\n')

db.insert('11', 1)
