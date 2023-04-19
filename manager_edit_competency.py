import sqlite3

connection = sqlite3.connect('RanchDatabase.db')
cursor = connection.cursor()

def update_competency(competency_id): 
    while True:
        manager_view = input( '\n\nWhat would you like to update?  \n\n[A] Edit Competency Name\n[B] Edit the date that the competency was created \n\n\n' )

        if manager_view == 'A':
            print ('~~~~~~Edit a Competency~~~~~~~')
            
            competency_value = input("Enter the name of the Competency: \n") 
            query = f"UPDATE Competencies SET name = ? WHERE competency_id = ?"
            cursor.execute(query, [competency_value, competency_id]) 
            connection.commit() #has to be above answer for it to print in database.  
            answer = input("Update another item? (y/n)  ")
                            
            if answer == "y":
              competency_id = input('Which competency would you like to update: \n\n ')
              update_competency(competency_id)
            if answer == "n":
              return

        if manager_view == 'B':
            print ('~~~~~~Edit a Competency~~~~~~~')
            
            competency_value = input("Enter the date that the Competency was created: \n") 
            query = f"UPDATE Competencies SET date_created = ? WHERE competency_id = ?"
            cursor.execute(query, [competency_value, competency_id]) 
            connection.commit() #has to be above answer for it to print in database.  
            answer = input("Update another item? (y/n)  ")
                            
            if answer == "y":
              competency_id = input('Which competency would you like to update: \n\n ')
              update_competency(competency_id)
            if answer == "n":
              return
        

        competency_value = ['']
        query = ''
    