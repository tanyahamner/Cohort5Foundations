import sqlite3
# from ManagerMenu import mangmenu
# from new_login_function import  user_manager
connection = sqlite3.connect('RanchDatabase.db')

cursor = connection.cursor()
 
def logout():
    
    print('\n\n                   ~~~~~~~~~~Thankyou for your time at the Ranch~~~~~~~\n')
    print('\n                           ~~~~~~~You are officially logged out~~~~~~~\n')
   

        

   