import sqlite3 as sql
import os
import csv
from sqlite3 import Error


def export_person(person_id): 

  conn=sql.connect('RanchDatabase.db')
  

 # Export data into CSV file
  print ('******Ranch User Data*******')
  print ('Exporting data into CSV............')
  cursor = conn.cursor()
  rows = cursor.execute("select * from Assessment_Results where person_id = ?", (person_id,)).fetchall()
  with open("person_results_data.csv", "w") as csv_file:
      
      csv_writer = csv.writer(csv_file, delimiter="\t", )
      csv_writer.writerow([i[0] for i in cursor.description])
      csv_writer.writerows(rows)

  dirpath = os.getcwd() +  "/person_results_data.csv"
  print ('Data exported Successfully into {}".format(dirpath)')

