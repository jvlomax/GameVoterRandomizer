__author__ = 'george'

import sqlite3
import os
import json

class dbHandler:
    def __init__(self):
        self.dbName = "database.sql"
        self.tableName = "games"

        if self.dbName in os.listdir:
            os.unlink(self.dbName)

        self.conn = sqlite3.connect(self.dbName)
        cursor = self.conn.cursor()

        cursor.exec('''CREATE TABLE {} (id PRIMARY KEY, title VARCHAR(255) NOT NULL, likes TEXT, numLikes INT)'''.format(self.tableName))


    def add_game(self, title):
        cursor = self.conn.cursor()
        cursor.exec('''INSERT INTO {} VALUES (NULL, {}, "[]", 0 )'''.format(self.tableName, title))
        self.conn.commit()
        cursor.close()

    def add_like(self, title, user):
        cursor = self.conn.cursor()
        likes = []
        numLikes = 0
        for row in cursor.exec('''SELECT likes, numLikes FROM {} WHERE title={}'''.format(self.tableName, title)):
            likes = json.loads(row[0])
            numLikes = row[1]
        if user in likes:
            return
        likes.append(user)
        numLikes += 1
        cursor.execute('''UPDATE {) SET likes={}, numLikes= WHERE title={}'''.format(self.tableName, likes, numLikes, title)



    def remove_game(self, title):
        cursor = self.conn.cursor()
        cursor.execute('''DELETE FROM {} WHERE title={}'''.format(self.tableName, title))
        self.conn.commit()
        cursor.close()

    def remove_like(self, title, user):


