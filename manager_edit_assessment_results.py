import sqlite3

connection = sqlite3.connect('RanchDatabase.db')
cursor = connection.cursor()

def update_assessment_result(assessment_result_id): 
    while True:
        manager_view = input( '\n\nWhat would you like to update?  \n\n[A] Edit Score\n[B] Edit the date that the assessment test was taken\n[C] Edit the time that the assessment test was taken\n[D] Edit the manager id of the results\n[E] Edit the person id that took the results\n[F] Edit the competency id of the result\n[G] Edit the assessment id of the results\n\n\n' )

        if manager_view == 'A':
            print ('~~~~~~Edit a Assessment Result~~~~~~~')
            
            result_value = input("Enter the score: \n") 
            query = f"UPDATE Assessment_Results SET score = ? WHERE assessment_results_id = ?"
            cursor.execute(query, [result_value, assessment_result_id]) 
            connection.commit() #has to be above answer for it to print in database.  
            answer = input("Update another item? (y/n)  ")
                            
            if answer == "y":
              assessment_result_id = input('Which assessment result id would you like to update: \n\n ')
              update_assessment_result(assessment_result_id)
            if answer == "n":
                return

        if manager_view == 'B':
            print ('~~~~~~Edit a Assessment Result~~~~~~~')
            
            result_value = input("Enter the date taken: \n") 
            query = f"UPDATE Assessment_Results SET date_taken = ? WHERE assessment_results_id = ?"
            cursor.execute(query, [result_value, assessment_result_id]) 
            connection.commit() #has to be above answer for it to print in database.  
            answer = input("Update another item? (y/n)  ")
                            
            if answer == "y":
              assessment_result_id = input('Which assessment result id would you like to update: \n\n ')
              update_assessment_result(assessment_result_id)
            if answer == "n":
                return
        
        if manager_view == 'C':
            print ('~~~~~~Edit a Assessment Result~~~~~~~')
            
            result_value = input("Enter the time taken: \n") 
            query = f"UPDATE Assessment_Results SET time_taken = ? WHERE assessment_results_id = ?"
            cursor.execute(query, [result_value, assessment_result_id]) 
            connection.commit() #has to be above answer for it to print in database.  
            answer = input("Update another item? (y/n)  ")
                            
            if answer == "y":
              assessment_result_id = input('Which assessment result id would you like to update: \n\n ')
              update_assessment_result(assessment_result_id)
            if answer == "n":
                return

        if manager_view == 'D':
            print ('~~~~~~Edit a Assessment Result~~~~~~~')
            
            result_value = input("Enter the manager id: \n") 
            query = f"UPDATE Assessment_Results SET manager_id = ? WHERE assessment_results_id = ?"
            cursor.execute(query, [result_value, assessment_result_id]) 
            connection.commit() #has to be above answer for it to print in database.  
            answer = input("Update another item? (y/n)  ")
                            
            if answer == "y":
              assessment_result_id = input('Which assessment result id would you like to update: \n\n ')
              update_assessment_result(assessment_result_id)
            if answer == "n":
                return
           
        if manager_view == 'E':
            print ('~~~~~~Edit a Assessment Result~~~~~~~')
            
            result_value = input("Enter the person id taken: \n") 
            query = f"UPDATE Assessment_Results SET person_id = ? WHERE assessment_results_id = ?"
            cursor.execute(query, [result_value, assessment_result_id]) 
            connection.commit() #has to be above answer for it to print in database.  
            answer = input("Update another item? (y/n)  ")
                            
            if answer == "y":
              assessment_result_id = input('Which assessment result id would you like to update: \n\n ')
              update_assessment_result(assessment_result_id)
            if answer == "n":
                return
        
        if manager_view == 'F':
            print ('~~~~~~Edit a Assessment Result~~~~~~~')
            
            result_value = input("Enter the competency id: \n") 
            query = f"UPDATE Assessment_Results SET competency_id = ? WHERE assessment_results_id = ?"
            cursor.execute(query, [result_value, assessment_result_id]) 
            connection.commit() #has to be above answer for it to print in database.  
            answer = input("Update another item? (y/n)  ")
                            
            if answer == "y":
              assessment_result_id = input('Which assessment result id would you like to update: \n\n ')
              update_assessment_result(assessment_result_id)
            if answer == "n":
                return

        if manager_view == 'G':
            print ('~~~~~~Edit a Assessment Result~~~~~~~')
            
            result_value = input("Enter the assessment id: \n") 
            query = f"UPDATE Assessment_Results SET assessment_id = ? WHERE assessment_results_id = ?"
            cursor.execute(query, [result_value, assessment_result_id]) 
            connection.commit() #has to be above answer for it to print in database.  
            answer = input("Update another item? (y/n)  ")
                            
            if answer == "y":
              assessment_result_id = input('Which assessment result id would you like to update: \n\n ')
              update_assessment_result(assessment_result_id)
            if answer == "n":
                return

     
        result_value = ['']
        query = ''
    