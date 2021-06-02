import sqlite3
from db import db


class UserModel(db.Model):
    __tablename__ = 'users'

    id = db.Column(db.Integer, primary_key=True)
    username = db.Column(db.String(80))
    password = db.Column(db.String(80))

    def __init__(self,_id,username,password):
        self.id = _id
        self.username = username
        self.password = password
        self.something = "hi"


    @classmethod
    def find_by_username(cls, username):
        connection = sqlite3.connect('data.db')
        cursor = connection.cursor()

        query = "SELECT * FROM users WHERE username=?"
        result = cursor.execute(query, username)
        row = result.fetchone()
        if row:
            user = cls(*row)
        else:
            user = None

        connection.close()
        return user

    @classmethod
    def find_by_id(cls, id):
        connection = sqlite3.connect('data.db')
        cursor = connection.cursor()

        query = "SELECT * FROM users WHERE id=?"
        result = cursor.execute(query, _id)
        row = result.fetchone()
        if row:
            user = cls(*row)
        else:
            user = None

        connection.close()

    @classmethod
    def insert(cls,item):
        conn = sqlite3.connect()
        cursor = conn.cusrsor()

        insert_query = "INSERT INTO items VALUES (?,?)"
        cursor.execute(insert_query, (item['name'],item['price']))

        conn.commit()
        conn.close()


        return user
