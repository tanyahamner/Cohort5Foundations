import sqlite3
from Logout import logout
from manager_view_function import view_members, view_user_competencies, admin_all_scores
from manager_add_function import add_user, add_new_competency, add_assessments, add_assessment_results
from manager_edit_users import update_person
from manager_search import search_user, search_competency, search_assessment
from manager_export_users import export_users_data
from manager_export_competency import export_competency_data
from manager_export_results import export_results
from manager_export_person import export_person
from manager_edit_competency import update_competency
from manager_edit_assessment import update_assessment
from manager_edit_assessment_results import update_assessment_result
from manager_search import search_user, search_assessment, search_competency
from user_view_functions import user_view_assessment_results
from manager_import_function import import_csv

# from csv_results import import_score
connection = sqlite3.connect('RanchDatabase.db')

cursor = connection.cursor()
def mangmenu():
    print('\n\n                   ~~~~~~~Welcome Manager~~~~~~~\n')
    print('\n\n~~~~~~~We appreciate your willingness to help our apprentices~~~~~~~\n')
    while True:
        
        user = input('Please choose from the following options: \n\n[1] View database\n\n[2] Edit User Profiles \n\n[3] Edit a Competencies\n\n[4] Edit an Assessment\n\n[5] Edit an assessment result\n\n[6] Search for a certain Person \n\n[7] Search for a competency\n\n[8] Search for an assessment\n\n[9] Add Information to the database\n\n[10] Delete an assessment result\n\n[11] Import Assessment Results\n\n[12] Export a list of Users\n\n[13] Export a list of Competencies\n\n[14] Export a result for a specific user\n\n[15] Export a list of all assessment results\n\n[16] Log Out\n\n[Q] Quit \n\n')

        if user == '1': #View Database
    
            print('\n~~~~~View the Database~~~~~\n')
            while True:
                manager_view = input( '\n\nWhat would you like to view?  \n\n[A] View Users of the Ranch\n[B] View all user competencies by User ID\n[C] View all user assessments by Assessment ID\n[D] View a report of all users and their competency levels for a given competency\n[R] Return to Main Menu\n\n' )

                if manager_view == 'A':
                    print ('~~~~~~The Ranch~~~~~~~')
                    view_members()
                elif manager_view == 'B':
                    print ('~~~~~~View all the Ranch user competencies~~~~~~~')
                    person_id = input('Please enter user id: \n')
                    user_view_assessment_results(person_id)
                elif manager_view == 'C':
                    print ('~~~~~~View all the Ranch user assessments~~~~~~~')
                    assessment_id = input('Please enter assessment id: \n')
                    view_user_competencies(assessment_id)
                elif manager_view == 'D':
                    print ('~~~~~~View the Ranch report of all users and their competency levels for a given competency~~~~~~~')
                    admin_all_scores()
                elif manager_view == 'R':
                    break
        elif user == '2': #edit/user profile
            print ('~~~~~~How would you like to update user profiles?~~~~~~~')
            person_id = input('Which person id would you like to update: \n\n')
            update_person(person_id)
            
        elif user == '3': #edit/competency
            print ('~~~~~~How would you like to update a competency?~~~~~~~')
            competency_id = input('Enter the competency id you want to update: \n\n')
            update_competency(competency_id)
            break
        elif user == '4': #edit/assessment
            print ('~~~~~~How would you like to update an assessment?~~~~~~~')
            assessment_id = input('Enter the assessment id you want to update: \n\n')
            update_assessment(assessment_id)
            break
        elif user == '5': #edit/assessment_result
            print ('~~~~~~How would you like to update an assessment result?~~~~~~~')
            assessment_result_id = input('Enter the assessment id you want to update: \n\n')
            update_assessment_result(assessment_result_id)
            break
        elif user == '6': #SearchUsers
            print ('~~~~~~Search the Ranch~~~~~~~')
            search_user()
            break
        elif user == '7': #Search competency
            print ('~~~~~~Search the Ranch~~~~~~~')
            search_competency()
            break
        elif user == '8': #Search assessment
            print ('~~~~~~Search the Ranch~~~~~~~')
            search_assessment()
            break
        elif user == '9': #Add Information to database
            print ('~~~~~~Add information to the Ranch Database~~~~~~~')
            while True:
                manager_view = input( '\n\nWhat would you like to add?  \n\n[A] Add a User to the Ranch\n[B] Add a new Competency \n[C] Add a New Assessment to a Competency\n[D] Add an Assessment result for a User for an Assessment \n[R]Return to Main Menu\n\n' )

                if manager_view == 'A':
                    print ('~~~~~~Add a New Member to the Ranch~~~~~~~')
                    add_user()
                    break
                elif manager_view == 'B':
                    print ('~~~~~~Add a new Competency~~~~~~~')
                    add_new_competency()
                    break
                elif manager_view == 'C':
                    print ('~~~~~~Add a New Assessment to a Competency~~~~~~~')
                    add_assessments()
                    break
                elif manager_view == 'D':
                    print ('~~~~~~Add an Assessment result for a User for an Assessment~~~~~~~')
                    add_assessment_results()
                    break
                elif manager_view == 'R':
                    break   
        elif user == '10':  #delete 
            delete_id = input("Please enter the assessment name that you need to remove from the database: \n ")
            # delete_result(delete_id)        
        elif user == '11': #Import
            print ('~~~~~~Import Assessment Results~~~~~~~')
            import_csv()
        elif user == '12': #Export users
            print ('~~~~~~Export Users~~~~~~~')
            export_users_data()
        elif user == '13': #Export Competencies
            print ('Export Competencies')
            export_competency_data()
        elif user == '14': #Export results for a specific user
            print ('~~~~~~Which user do you need to export data?~~~~~~~')
            person_id = input('Which person id that you would like to export: \n\n')
            export_person(person_id)
            break
        elif user == '15': #Export Assessment Results
            print ('~~~~~~Export Assessment Results~~~~~~~')
            export_results()

            
        elif user == '16':
            logout()
            break

        if user == 'Q':
            print("I hope you saw everything you need to see about your coworkers and clients. If anything you notice is wrong, please let me know.")
            break

        connection.commit()

