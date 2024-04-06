import sqlite3
import os

class LoginPass:
    def __init__(self):
        if not os.path.exists('loginPass.db'):
            self.conn = sqlite3.connect('loginPass.db')
            self.cursor = self.conn.cursor()
            self.create_table()
            print('Таблица создана')
        else:
            print('Таблица уже есть')
            self.conn = sqlite3.connect('loginPass.db')     
            self.cursor = self.conn.cursor()
            
    def create_table(self):
        self.cursor.execute('''CREATE TABLE IF NOT EXISTS loginPass
                              (id INTEGER PRIMARY KEY,
                               name TEXT,
                               email TEXT,
                               password TEXT)''')
        self.conn.commit()

    def add_entry(self, name, email, password):
        try:
            self.cursor.execute('''INSERT INTO loginPass (name, email, password)
                              VALUES (?, ?, ?)''', (name, email, password))
            self.conn.commit()
        except sqlite3.Error as e:
            print(e)

    def get_all_entries(self):
        try:
            self.cursor.execute('''SELECT * FROM loginPass''')
            return self.cursor.fetchall()
        except sqlite3.Error as e:
            print(e)

    def get_entry_by_name(self, name):
        try:
            self.cursor.execute('''SELECT * FROM loginPass WHERE name = ?''', (name,))
            return self.cursor.fetchone()
        except sqlite3.Error as e:
            print(e)

    def get_entry_by_email(self, email):
        try:
            self.cursor.execute('''SELECT * FROM loginPass WHERE email = ?''', (email,))
            return self.cursor.fetchone()
        except sqlite3.Error as e:
            print(e)

    def update_entry(self, name, email, password):
        try:
            self.cursor.execute('''UPDATE loginPass SET email = ?, password = ?
                              WHERE name = ?''', (email, password, name))
            self.conn.commit()
        except sqlite3.Error as e:
            print(e)

    def delete_entry_by_name(self, name):
        try:
            self.cursor.execute('''DELETE FROM loginPass WHERE name = ?''', (name,))
            self.conn.commit()
        except sqlite3.Error as e:
            print(e)

    def delete_entry_by_email(self, email):
        try:
            self.cursor.execute('''DELETE FROM loginPass WHERE email = ?''', (email,))
            self.conn.commit()
        except sqlite3.Error as e:
            print(e)

    def __del__(self):
        self.conn.close()

def console_interface():
    print('''
    =================================
    | Bridge Password Manager v0.1  |
    =================================''')
    print('''
    What do you want to do?
    (1) Register
    (2) Login
    (3) Exit''')
    choice = input('>>> ')
    
    loginPass = LoginPass()
    if choice == '1':
        name = input('Enter your name: ')
        email = input('Enter your email: ')
        password = input('Enter your password: ')
        loginPass.add_entry(name, email, password)
        print('Registration Successful!')
    elif choice == '2':
        email = input('Enter your email: ')
        tries = 3
        while tries:
            password = input('Enter your password: ')
            entry = loginPass.get_entry_by_email(email)
            if entry[3] == password and entry[2] == email:
                print('Login Successful!')
                break
            else:
                tries -= 1
                if tries == 0:
                    print('Login Failed! You have no more tries.')
                    break
                print('Login Failed! Try again.')
    elif choice == '3':
        print('Goodbye!')
    else:
        print('Invalid input!')
    print()
    console_interface()


if __name__ == '__main__':
    console_interface()