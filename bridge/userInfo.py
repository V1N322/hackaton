import sqlite3
import os

class UserInfo:
    def __init__(self):
        if not os.path.exists('userInfo.db'):
            self.conn = sqlite3.connect('userInfo.db')
            self.cursor = self.conn.cursor()
            self.create_table()
            print('Таблица создана')
        else:
            print('Таблица уже есть')
            self.conn = sqlite3.connect('userInfo.db')     
            self.cursor = self.conn.cursor()
            
    def create_table(self):
        self.cursor.execute('''CREATE TABLE IF NOT EXISTS userInfo
                              (id INTEGER PRIMARY KEY,
                               name TEXT,
                               age INTEGER,
                               is_admin INTEGER,
                               traveler_type TEXT,
                               is_gastranom INTEGER,
                               is_architecture INTEGER,
                               is_local_culture INTEGER,
                               is_nature INTEGER,
                               is_sport INTEGER,
                               is_rest INTEGER)''')
        self.conn.commit()

    def add_entry(self, name, age, is_admin, traveler_type, is_gastranom, is_architecture, is_local_culture, is_nature, is_sport, is_rest):
        try:
            self.cursor.execute('''INSERT INTO userInfo (name, age, is_admin, traveler_type, is_gastranom, is_architecture, is_local_culture, is_nature, is_sport, is_rest)
                                  VALUES (?, ?, ?, ?, ?, ?, ?, ?, ?, ?)''', (name, age, is_admin, traveler_type, is_gastranom, is_architecture, is_local_culture, is_nature, is_sport, is_rest))
            self.conn.commit()
        except sqlite3.Error as e:
            print(e)

    def get_all_entries(self):
        try:
            self.cursor.execute('''SELECT * FROM userInfo''')
            return self.cursor.fetchall()
        except sqlite3.Error as e:
            print(e)

    def get_entry_by_name(self, name):
        try:
            self.cursor.execute('''SELECT * FROM userInfo WHERE name = ?''', (name,))
            return self.cursor.fetchone()
        except sqlite3.Error as e:
            print(e)

    def get_entry_by_age(self, age):
        try:
            self.cursor.execute('''SELECT * FROM userInfo WHERE age = ?''', (age,))
            return self.cursor.fetchone()
        except sqlite3.Error as e:
            print(e)

    def update_entry(self, name, age, is_admin, traveler_type, is_gastranom, is_architecture, is_local_culture, is_nature, is_sport, is_rest):
        try:
            self.cursor.execute('''UPDATE userInfo SET age = ?, is_admin = ?, traveler_type = ?, is_gastranom = ?, is_architecture = ?, is_local_culture = ?, is_nature = ?, is_sport = ?, is_rest = ?
                                  WHERE name = ?''', (age, is_admin, traveler_type, is_gastranom, is_architecture, is_local_culture, is_nature, is_sport, is_rest, name))
            self.conn.commit()
        except sqlite3.Error as e:
            print(e)

    def delete_entry_by_name(self, name):
        try:
            self.cursor.execute('''DELETE FROM userInfo WHERE name = ?''', (name,))
            self.conn.commit()
        except sqlite3.Error as e:
            print(e)

    def delete_entry_by_age(self, age):
        try:
            self.cursor.execute('''DELETE FROM userInfo WHERE age = ?''', (age,))
            self.conn.commit()
        except sqlite3.Error as e:
            print(e)

    def __del__(self):
        self.conn.close()