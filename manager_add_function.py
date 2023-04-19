import sqlite3
import bcrypt

connection = sqlite3.connect('RanchDatabase.db')
cursor = connection.cursor()

def add_user():
    print('\n~~~~~Add a User to the Ranch~~~~~\n')
    first_name = input('Please enter a first name: ')
    last_name = input('Please enter a last name: ')
    phone = input('Please enter their phone number: ')
    email = input('Please enter their email: ')
    password = input('Please enter a password for the user: ')
    active = input('Please enter a 1 for active or 0 for deactive: ')
    date_created = input('Please enter the date this was created: ')
    hire_date = input('Please enter their hire date: ')
    user_type = input('Please enter User or Manager: ')
    hashed = bcrypt.hashpw(password.encode('utf-8'), bcrypt.gensalt())
    query = "INSERT INTO Users (first_name, last_name, phone, email, password, date_created, hire_date, user_type, active) VALUES (?, ?, ?, ?, ?, ?, ?, ?, ?)"
    values = [first_name, last_name, phone, email, hashed, date_created, hire_date, user_type, active]
   
    cursor.execute(query, values)
    connection.commit()

def add_new_competency():
    print('\n~~~~~Add a new competency to the Ranch~~~~~\n')
    name = input('Please enter the name of the competency: ')
    date_created = input('Please enter the date this was created: ')

    query = "INSERT INTO Competencies (name, date_created) VALUES (?, ?)"
    values = [name,  date_created]
   
    cursor.execute(query, values)
    connection.commit()


def add_assessments(): 
    print('\n~~~~~Add a new assessment to a competency to the Ranch~~~~~\n')
    name = input('Please enter the name of the new assessment: ')
    date_created = input('Please enter the date this was created: ')

    query = "INSERT INTO Assessments (name,  date_created) VALUES (?, ?)"
    Values = [name, date_created, ]
   
    cursor.execute(query, Values)
    connection.commit()



def add_assessment_results(): 
    print('\n~~~~~Add the assessment results to one of the Ranch members~~~~~\n')
    person_id = input('Please enter the user id of the person you are scoring: ')
    assessment_id = input('Please enter the assessment id: ')
    competency_id = input('Please enter the competency id: ')
    score = input('Please enter their score between 0 and 4: ')
    date_taken = input('Please enter the date this assessment was taken: ')
    time_taken = input('Please enter the time the member took the assessment: ')
    manager_id = input('Please enter your the user id: ')

    query = "INSERT INTO Assessment_Results (person_id, assessment_id, competency_id, score, date_taken, time_taken, manager_id) VALUES (?, ?, ?, ?, ?, ?, ?)"
    Values = [person_id, assessment_id, competency_id, score, date_taken, time_taken, manager_id]
   
    cursor.execute(query, Values)
    connection.commit()
