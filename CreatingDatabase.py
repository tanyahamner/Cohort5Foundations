import sqlite3

def create_schema(cursor):

  cursor.execute(''' CREATE TABLE IF NOT EXISTS Users(
    person_id INTEGER PRIMARY KEY AUTOINCREMENT,
    user_type TEXT,
    first_name TEXT NOT NULL,
    last_name TEXT,
    email TEXT UNIQUE NOT NULL,
    phone TEXT,
    password TEXT NOT NULL,
    date_created TEXT,
    hire_date TEXT,
    active INTEGER DEFAULT 1
    );''')

  cursor.execute(''' CREATE TABLE IF NOT EXISTS Competencies (
    competency_id INTEGER PRIMARY KEY AUTOINCREMENT,
    name TEXT,
    date_created TEXT
    );''')

  cursor.execute(''' CREATE TABLE IF NOT EXISTS Assessments(
    assessment_id INTEGER PRIMARY KEY AUTOINCREMENT,
    name TEXT, 
    date_created TEXT,
    competency_id INTEGER,
    FOREIGN KEY (name)
        REFERENCES Competencies(competency_id)
        );''')


  cursor.execute(''' CREATE TABLE IF NOT EXISTS Assessment_Results(
    assessment_results_id INTEGER PRIMARY KEY AUTOINCREMENT,
    score TEXT,
    date_taken TEXT,
    time_taken TEXT,
    manager_id INTEGER,
    person_id INTEGER,
    competency_id INTEGER,
    assessment_id INTEGER,
    FOREIGN KEY (manager_id)
        REFERENCES Users(person_id),
    FOREIGN KEY (person_id)
        REFERENCES Users(person_id),
    FOREIGN KEY (competency_id)    
        REFERENCES Competencies(competency_id),
    FOREIGN KEY (assessment_id)  
        REFERENCES Assessment(assessment_id)
        );''')


connection = sqlite3.connect('RanchDatabase.db')
cursor = connection.cursor()

result = create_schema(cursor)