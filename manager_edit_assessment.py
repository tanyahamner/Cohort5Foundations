import sqlite3

connection = sqlite3.connect('RanchDatabase.db')
cursor = connection.cursor()

def update_assessment(assessment_id): 
    while True:
        manager_view = input( '\n\nWhat would you like to update?  \n\n[A] Edit assessment Name\n[B] Edit the date that the assessment was created \n\n\n' )

        if manager_view == 'A':
            print ('~~~~~~Edit an assessment~~~~~~~')
            
            assessment_value = input("Enter the name of the assessment: \n") 
            query = f"UPDATE Assessments SET name = ? WHERE assessment_id = ?"
            cursor.execute(query, [assessment_value, assessment_id]) 
            connection.commit() #has to be above answer for it to print in database.  
            answer = input("Update another item? (y/n)  ")
                            
            if answer == "y":
              assessment_id = input('Which assessment would you like to update: \n\n ')
              update_assessment(assessment_id)
            if answer == "n":
                return

        if manager_view == 'B':
            print ('~~~~~~Edit an assessment~~~~~~~')
            
            assessment_value = input("Enter the date that the assessment was created: \n") 
            query = f"UPDATE Assessments SET date_created = ? WHERE assessment_id = ?"
            cursor.execute(query, [assessment_value, assessment_id]) 
            connection.commit() #has to be above answer for it to print in database.  
            answer = input("Update another item? (y/n)  ")
                            
            if answer == "y":
              assessment_id = input('Which assessment would you like to update: \n\n ')
              update_assessment(assessment_id)
            if answer == "n":
                return
        

           
     
        assessment_value = ['']
        query = ''
    