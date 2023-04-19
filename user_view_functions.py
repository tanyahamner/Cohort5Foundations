import sqlite3
import bcrypt

connection = sqlite3.connect('RanchDatabase.db')
cursor = connection.cursor()

#Viewing 


def user_profile(person_id):
    print('\n~~~Your Profile~~~\n')
   
    user = cursor.execute("SELECT first_name, last_name, phone, email, hire_date FROM Users WHERE person_id = ?", (person_id,)).fetchone()
    print (f"{'First Name':<20} {'Last Name':<20} {'Phone':<25} {'Email':<25} {'Hire Date'}\n")
    
    user = [str(x) for x in user]
            
    print(f'{user[0]:<20} {user[1]:<20} {user[2]:25} {user[3]:25} {user[4]}')

    connection.commit()

def user_view_assessment_results(person_id):
    print('\n~~~User Assessment Results~~~\n')
    user = cursor.execute("SELECT assessment_results_id, score, date_taken, time_taken, competency_id, assessment_id FROM Assessment_Results WHERE person_id = ?", (person_id, )).fetchone()
   
    print (f"{'Assessment Results ID':<25} {'Score':<15} {'Date Taken':<20} {'Time Taken':<20} {'Competency Id':<20} {'Assessment ID':<20}\n")
    
    user = [str(x) for x in user]
        
    print(f'{user[0]:<25} {user[1]:<15} {user[2]:20} {user[3]:20} {user[4]:20} {user[5]}')
# #           assessment result id   score   date taken   time taken  competency id   assessment id                       
    connection.commit()




def update_user_person(person_id):
    print('\n\n~~~~~~~~~~~~~~~~~~~~~~~~~~Welcome~~~~~~~~~~~~~~~~~~~~~~\n')
    print('\n\n~~~~~~~We appreciate your time at the Dream Team~~~~~~~\n')
    while True:
        user_view = input( '\n\nWhat would you like to update?  \n\n[A] Edit First Name\n[B] Edit Last Name \n[C] Edit Phone Number\n[D] Edit Email \n[E] Change your password \n[R] Return to Main Menu\n\n' )

        if user_view == 'A':  # update_person(update_user)
            print ('~~~~~~Edit your first name~~~~~~~')
            
            update_value = input("Enter the updated first name: \n") 
            query = f"UPDATE Users SET first_name = ? WHERE person_id = ?"
            cursor.execute(query, [update_value,person_id]) 
            connection.commit() #has to be above answer for it to print in database.  



        elif user_view == 'B':  # update_person(person_id)
            print ('~~~~~~Edit your last name~~~~~~~')
            
            update_value = input("Enter the updated last name: \n") 
            query = f"UPDATE Users SET last_name = ? WHERE person_id = ?"
            cursor.execute(query, [update_value,person_id])  
            connection.commit() #has to be above answer for it to print in database.  

        elif user_view == 'C':
            print ('~~~~~~Edit your Phone~~~~~~~')
            update_value = input("Enter the updated phone number: \n") 
            query = f"UPDATE Users SET phone = ? WHERE person_id = ?"
            cursor.execute(query, [update_value,person_id]) 
            connection.commit()

        elif user_view == 'D':
            print ('~~~~~~Edit your Email~~~~~~~')
            update_value = input("Enter the updated email: \n") 
            query = f"UPDATE Users SET email = ? WHERE person_id = ?"
            cursor.execute(query, [update_value,person_id]) 
            connection.commit()

        elif user_view == 'E':
            print ('~~~~~~Edit your Password~~~~~~~')
            update_value = input('Please enter your new password: \n')
            query = f"UPDATE Users SET password = ? WHERE person_id = ?"
            hashed = bcrypt.hashpw(update_value.encode('utf-8'), bcrypt.gensalt())
            cursor.execute(query, [hashed, person_id, ]) 

            connection.commit()

        elif user_view == 'R':
            return
        update_value = ['']
        query = ''

connection.commit()