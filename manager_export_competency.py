import sqlite3 as sql
import os
import csv
from sqlite3 import Error

def export_competency_data():

  # Connect to database
  conn=sql.connect('RanchDatabase.db')

  
 # To view table data in table format
  print ('******Ranch User Data*******')
  cur = conn.cursor()
  cur.execute('''SELECT * FROM Competencies''')
  rows = cur.fetchall()
   
  for row in rows:
      print(row)

 # Export data into CSV file
  print ('Exporting data into CSV............')
  cursor = conn.cursor()
  rows = cursor.execute("select * from Competencies").fetchall()
  with open("competency_data.csv", "w") as csv_file:
      csv_writer = csv.writer(csv_file, delimiter="\t")
      csv_writer.writerow([i[0] for i in cursor.description])
      csv_writer.writerows(rows)

  dirpath = os.getcwd() +  "/competency_data.csv"
  print ('Data exported Successfully into {}".format(dirpath)')

