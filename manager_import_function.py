import sqlite3
import csv

connection = sqlite3.connect('RanchDatabase.db')
cursor = connection.cursor()

def import_csv():

    with open('results_to_be_imported.csv', 'r') as csvfile:
        data = csv.reader(csvfile)
        header = next(data)
        query = "INSERT INTO Assessment_Results (score, date_taken, time_taken, manager_id, person_id, competency_id, assessment_id) VALUES (?, ?, ?, ?, ?, ?, ?)"
        if header != None:

            for row in data:
                cursor.execute(query, row[1::])

        connection.commit()
