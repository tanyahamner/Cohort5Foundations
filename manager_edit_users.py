import sqlite3
import bcrypt

connection = sqlite3.connect('RanchDatabase.db')
cursor = connection.cursor()

def update_person(person_id): 
    while True:
        manager_view = input( '\n\nWhat would you like to update?  \n\n[A] Edit a Users First Name\n[B] Edit a Users Last Name \n[C] Edit a email\n[D] Edit a phone number \n[E] Activate User\n[F] Deactivate User\n[P] Update a password\n\n\n' )

        if manager_view == 'A':  # update_person(update_user)
            print ('~~~~~~Edit a Ranch User~~~~~~~')
            update_value = input("Enter the updated first name: \n") 
            query = f"UPDATE Users SET first_name = ? WHERE person_id = ?"
            cursor.execute(query, [update_value, person_id]) 
            connection.commit() #has to be above answer for it to print in database.  
            answer = input("Update another item? (y/n)  ")
                            
            if answer == "y":
                person_id = input('Which person would you like to update person_id b: \n\n ')
                update_person(person_id)
            if answer == "n":
                return

        if manager_view == 'B':  # update_person(update_user)
            print ('~~~~~~Edit a Ranch User~~~~~~~')
            update_value = input("Enter the updated last name: \n") 
            query = f"UPDATE Users SET last_name = ? WHERE person_id = ?"
            cursor.execute(query, [update_value, person_id]) 
            connection.commit() #has to be above answer for it to print in database.  
            answer = input("Update another item? (y/n)  ")
                            
            if answer == "y":
                person_id = input('Which person would you like to update person_id: \n\n ')
                update_person(person_id)
            if answer == "n":
                return

        elif manager_view == 'C':
            
            update_value = input("Enter the updated email: \n") 
            query = f"UPDATE Users SET email = ? WHERE person_id = ?"
            cursor.execute(query, [update_value, person_id]) 
            connection.commit() #has to be above answer for it to print in database.  
            answer = input("Update another item? (y/n)  ")
                            
            if answer == "y":
                person_id = input('Which person would you like to update person_id: \n\n ')
                update_person(person_id)
            if answer == "n":
                return
            
        elif manager_view == 'D':
            
            update_value = input("Enter the updated phone number: \n") 
            query = f"UPDATE Users SET phone = ? WHERE person_id = ?"
            cursor.execute(query, [update_value, person_id]) 
            connection.commit() #has to be above answer for it to print in database.  
            answer = input("Update another item? (y/n)  ")
                            
            if answer == "y":
                person_id = input('Which person would you like to update person_id: \n\n ')
                update_person(person_id)
            if answer == "n":
                return
        elif manager_view == 'E': #activate
            
            update_value = input("Enter 1 to activate user: \n") 
            query = f"UPDATE Users SET active = 1 WHERE person_id = ?"
            cursor.execute(query, [person_id]) 
            connection.commit() 
            answer = input("Update another item? (y/n)  ")
                            
            if answer == "y":
                person_id = input('Which person would you like to update person_id: \n\n ')
                update_person(person_id)
            if answer == "n":
                return
            
        elif manager_view == 'F': #deactivate
            
            update_value = input("Enter 0 to deactivate user: \n") 
            query = f"UPDATE Users SET active = 0 WHERE person_id = ?"
            cursor.execute(query, [person_id]) 
            connection.commit() 
            answer = input("Update another item? (y/n)  ")
                            
            if answer == "y":
                person_id = input('Which person would you like to update person_id: \n\n ')
                update_person(person_id)
            if answer == "n":
                return
            
        elif manager_view == 'P':
            print ('~~~~~~Edit your Password~~~~~~~')
            update_value = input('Please enter your new password: \n')
            query = f"UPDATE Users SET password = ? WHERE person_id = ?"
            hashed = bcrypt.hashpw(update_value.encode('utf-8'), bcrypt.gensalt())
            cursor.execute(query, [hashed, person_id, ]) 
            connection.commit()
            answer = input("Update another item? (y/n)  ")
                            
            if answer == "y":
                person_id = input('Which person would you like to update person_id: \n\n ')
                update_person(person_id)
            if answer == "n":
                return
            
     
connection.commit()
   