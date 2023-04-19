import sqlite3

connection = sqlite3.connect('RanchDatabase.db')
cursor = connection.cursor()

def search_user():
    search = input('Please enter a first name or a last name:\n\n')

    query = "SELECT person_id, first_name, last_name, phone, email, hire_date, user_type  FROM Users WHERE first_name LIKE ? OR last_name LIKE ?"
    rows = cursor.execute(query, (f'%{search}%', f'%{search}%')).fetchall()

    print('\n~~~~Members~~~~')
    
    info_data = ['person_id', 'first_name', 'last_name', 'phone', 'email', 'hire_date', 'user_type,  ']
    print (f" {'Person ID':<5} {'First name':<15} {'Last name':<17} {'Phone':<18} {'Email':<15} {'Hire Date':<23}{'Manager'}\n")
    
    for info_data in rows:
        info_data = [str(info) for info in info_data]
        print(f' {info_data[0]:<7}{info_data[1]:<15}{info_data[2]:<15}{info_data[3]:<15}{info_data[4]:<23}{info_data[5]:<25}{info_data[6]}')
#                    id              first name         last name       phone                email          hire date        user type                      
def search_competency():
    searchcompetency = input('Please enter a name or id of competency:\n\n')

    query = "SELECT competency_id, name, date_created  FROM Competencies WHERE name LIKE ? OR competency_id LIKE ?"
    rows = cursor.execute(query, (f'%{searchcompetency}%', f'%{searchcompetency}%')).fetchall()

    print('\n~~~~Competencies~~~~')
    
    info_data = ['competency_id', 'name', 'date_created']
    print (f" {'Competency ID':<5} {'Name':<15} {'Date Created':<17}\n")
    
    for info_data in rows:
        info_data = [str(info) for info in info_data]
        print(f' {info_data[0]:<7}{info_data[1]:<15}{info_data[2]:<15}')
#                    id              first name         last name       phone                email          hire date        user type                      

def search_assessment():
    searchassessment = input('Please enter a name or id of assessment:\n\n')

    query = "SELECT assessment_id, name, date_created  FROM Assessments WHERE name LIKE ? OR assessment_id LIKE ?"
    rows = cursor.execute(query, (f'%{searchassessment}%', f'%{searchassessment}%')).fetchall()

    print('\n~~~~Competencies~~~~')
    
    info_data = ['assessment_id', 'name', 'date_created']
    print (f" {'Assessment ID':<5} {'Name':<15} {'Date Created':<17}\n")
    
    for info_data in rows:
        info_data = [str(info) for info in info_data]
        print(f' {info_data[0]:<7}{info_data[1]:<15}{info_data[2]:<15}')
#                    id              first name         last name       phone   

