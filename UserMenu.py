import sqlite3
from user_view_functions import user_profile, user_view_assessment_results, update_user_person
from Logout import logout
# from edit_user_function import update_userperson
connection = sqlite3.connect('RanchDatabase.db')

cursor = connection.cursor()
def user_menu(person_id):
    print('\n\n  ~~~~~~~~~~~~~~~Welcome User~~~~~~~\n')
    print('\n\n~~~~~~~We appreciate your time here~~~~~~~\n')
   
    while True:
        
        user = input('What would you like to do\n\n[1] View your profile\n\n[2] Update your profile \n\n[3] Logout \n\n[Q] Quit \n\n')
    
        if user == '1': #View Profile
    
            print('\n~~~~~Your Profile~~~~~\n')
            while True:
                user_view = input( '\n\nWhat would you like to view?  \n\n[A] View Your Profile\n\n[B] Your Assessments\n\n[R] Return to Main Menu\n\n' )

                if user_view == 'A':
                    print ('~~~~~~Your Profile~~~~~~~')
                    user_profile(person_id)

                elif user_view == 'B':
                    print ('~~~~~~Your Assessments~~~~~~~')
                    user_view_assessment_results(person_id)
                elif user_view == 'R':
                    break
                
        elif user == '2':
            print ('~~~~~~Update your profile~~~~~~~')
            print(f"Person ID :{person_id}")
            update_user_person(person_id)

        elif user == '3':
            logout()
            break
        if user == 'Q':
            print("Thank you for your commitment to the Ranch.")
            break
        
        connection.commit()

   