import sqlite3

connection = sqlite3.connect('capstone.db')
cursor = connection.cursor()

def comptency_info(name):
    query = "SELECT name, date_created FROM Competencies WHERE name=?"
    info = cursor.execute(query, [name]).fetchone()
    ('\n~~~Information~~~')
    print(f"Name:     {info[0]}")
    print(f"Date Created: {info[1]}")

def assessment_info(name):
    query = "SELECT name, competency, date_created FROM Assessments WHERE name=?"
    info = cursor.execute(query, [name]).fetchone()
    ('\n~~~Information~~~')
    print(f"Name:     {info[0]}")
    print(f"Competency: {info[1]}")
    print(f"Date Created: {info[1]}")

def result_info(user_id):
    query = "SELECT user_id, first_name, last_name, assessment, score, date_taken, time taken FROM Assessment_Result WHERE user_id=?"
    info = cursor.execute(query, [user_id]).fetchone()
    
    full_name = f'{info[1]} {info[2]}'
    ('\n~~~Information~~~')
    print(f"User ID:     {info[0]}")
    print(f"Name: {full_name}")
    print(f"Assessment: {info[3]}")    
    print(f"Date Taken:     {info[4]}")
    print(f"Time Taken: {info[5]}")
    print(f"Manager ID: {info[6]}")