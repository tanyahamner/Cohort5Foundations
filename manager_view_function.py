import sqlite3

connection = sqlite3.connect('RanchDatabase.db')
cursor = connection.cursor()


def view_members():
    print('\n~~~Members of the Ranch~~~\n')
    rows = cursor.execute("SELECT person_id, user_type, first_name, last_name, email, phone, hire_date,  active FROM Users ").fetchall()
    info_data = ['person_id', 'user_type', 'first_name', 'last_name', 'email', 'phone', 'hire_date', 'active']
    print (f" {'Person Id':<15} {'User Type':<15} {'First name':<16} {'Last name':<16} {'Email':<27} {'Phone':<15} {'Hire Date':<15} {'Active':<5}\n")
    
    for info_data in rows:
        info_data = [str(info) for info in info_data]
        print(f' {info_data[0]:<17}{info_data[1]:<15}{info_data[2]:<17}{info_data[3]:<17}{info_data[4]:<28}{info_data[5]:<16}{info_data[6]:<20}{info_data[7]}')
#                    id                user type        first name         last name       email                phone           hire date                active             
def view_user_competencies(assessment_id):
    print('\n~~~Members of the Ranch~~~\n')
    rows = cursor.execute("SELECT U.person_id, first_name, last_name, email, phone, AR.assessment_id FROM Assessment_Results AR JOIN Users U ON AR.person_id = U.person_id WHERE AR.assessment_id = ?", (assessment_id,)).fetchall()
    info_data = ['person_id', 'first_name', 'last_name', 'email', 'phone', 'assessment_id']
    print (f" {'Person ID':<15} {'First name':<16} {'Last name':<16} {'Email':<27} {'Phone':<15} {'Assessment ID'}\n")
    
    for info_data in rows:
        info_data = [str(info) for info in info_data]
        print(f' {info_data[0]:<16}{info_data[1]:<17}{info_data[2]:<17}{info_data[3]:<28}{info_data[4]:<17}{info_data[5]}')
#                 id              first name         last name       email                phone           Assessment                            

def admin_competencies_users(competency_id):
    print('\n~~~Courses~~~\n')
    rows = cursor.execute("SELECT person_id, competency_id, score, date_taken, time_taken FROM Assessment_Results WHERE person_id=?", (competency_id,)).fetchall()
    info_data = ['person_id', 'competency_id', 'score', 'date_taken', 'time_taken']
    print (f" {'person_id':<15} {'competency_id':<16}{'score':<16}{'date_taken':<16}{'time_taken'}\n")
    
    for info_data in rows:
        info_data = [str(info) for info in info_data]
        print(f' {info_data[0]:<16}{info_data[1]:<16}{info_data[2]:<16}{info_data[3]:<16}{info_data}')
#                  person_id         competency_id         score          date_taken         time_taken                  
def admin_all_scores():
    print('\n~~~All Assessment Results~~~\n')
    rows = cursor.execute("SELECT assessment_results_id, score, date_taken, time_taken, manager_id, person_id, competency_id, assessment_id FROM Assessment_Results ").fetchall()
    info_data = ['assessment_results_id', 'score', 'date_taken', 'time_taken', 'manager_id', 'person_id', 'competency_id', 'assessment_id']
    print (f" {'Assessment Results Id':<27} {'Score':<15} {'Date Taken':<16} {'Time Taken':<16} {'Manager ID':<27} {'Person ID':<15} {'Competency ID':<15} {'Assessment ID':<15}\n")
    
    for info_data in rows:
        info_data = [str(info) for info in info_data]
        print(f' {info_data[0]:<28}{info_data[1]:<16}{info_data[2]:<17}{info_data[3]:<19}{info_data[4]:<28}{info_data[5]:<16}{info_data[6]:<20}{info_data[7]:<20}')
#           assessment results id   score              date taken        time taken        manager id           person id      competency id     assessment id     active             
