import sqlite3
import bcrypt
from UserMenu import user_menu
from ManagerMenu import mangmenu
connection = sqlite3.connect('RanchDatabase.db')
cursor = connection.cursor()



def user_manager():
    user_name = input("\nPlease enter your email: ")
    password = input("\nPlease enter your password: ")
    row = cursor.execute("SELECT person_id, password, user_type FROM Users WHERE email=? AND active = 1", (user_name,)).fetchone()
    print(row)
    if not row:
        return (print("Wrong credentials"))
    db_password = row[1]
    user_type = row[2]
    person_id = row[0]
    password_encoded = password.encode("utf-8")
    hashed = bcrypt.checkpw(password_encoded, db_password)
    if hashed and (user_type == 'Manager'):
        mangmenu()
    elif hashed and (user_type == 'User'):
        user_menu(person_id)
    else:
        return(
            print("Incorrect Credentials")
        )