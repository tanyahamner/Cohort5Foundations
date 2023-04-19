import sqlite3
# from ManagerMenu import mangmenu
from Login import  user_manager
connection = sqlite3.connect('RanchDatabase.db')

cursor = connection.cursor()
 
def welcome_menu():
    
    print('\n\n                              ~~~~~~~~~~~~~~~Welcome to the Ranch~~~~~~~\n')
    print('\n                              ~~~~~~~We appreciate your time here~~~~~~~\n')
    print('\n\nHere at the Ranch you will grow as a web developer and learn how to code specifically for agriculture.  \nAt the end of your training your manager will fill out your competency assessment and depending on your \nassessment will determine if you continue on full time or stay as an apprenticeship.')
  
    user = input(f'\nEnter:\n\n[1] If you are a Manager\n\n[2] If you are a User \n\n[Q] Quit \n\n')
     
    while True:
           
        if user == '1':
            user_manager()
            # mangmenu()

            break
        elif user == '2':
            # user_login()
            user_manager()
            break
    
        elif user == 'Q':
            print("\nThank you for your commitment to the Ranch.")
            break
        
        else:
            break
        
welcome_menu()
   