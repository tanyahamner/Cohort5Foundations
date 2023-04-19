import sqlite3

connection = sqlite3.connect('RanchDatabase.db')

cursor = connection.cursor()

def delete(person_id):
    results = f'DELETE FROM Assesment_Results WHERE person_id = {person_id}'
    cursor.execute(results, person_id)
    # query = f'DELETE '
    # connection = sqlite3.connect('RanchDatabase.db')

    # db.cursor = ConnectionResetError.cursor()
    # db.cursor.execute("begin")
    # print("Assessment Result Deleted")
    # db_cursor.executed("back")
    # connection.commit()