import sqlite3
import csv
# with open('ranchusers.csv', 'r') as myfile:
#     # header_row = myfile.readline()
#     # split_header = header_row.strip('\n').split(',')
#     reader = csv.reader(myfile)
#     reader.
#     person_id = 'PERSON ID'
#     user_type = 'USER TYPE'
#     first_name = 'FIRST NAME'
#     last_name = 'LAST NAME'
#     email = 'EMAIL'
#     phone = 'PHONE'
#     date_created = 'DATE CREATED'
#     hire_date = 'HIRE DATE'
#     active = 'ACTIVE'
#     print('')
#     print('')
#     print('')
#     print(f'{split_header[0]:24} {split_header[1]:10} {split_header[2]:10} {split_header[2]:10} {split_header[2]:10} {split_header[2]:10} {split_header[2]:10} {split_header[2]:10} {split_header[2]:10} ')
#     print('------------------     ---------  ---------  ---------  --------- \n')

#     my_lines = myfile.readlines()       
#     for lines in my_lines:
#         line = lines.split(',')
        
#         county = line[0]
#         pop_2010 = line[1]
#         pop_2019 = line[-1].strip('\n')
#         growth_data = int(pop_2019) - int(pop_2010)
#         rate_data = (int(growth_data) / int(pop_2019)) * 100

#         print(f'{county:24} {pop_2010:10} {pop_2019:10} {growth_data:6} {rate_data:>8.2f} %')
#         print('')
connection = sqlite3.connect('RanchDatabase.db')
cursor = connection.cursor()

def import_csv():
    data_list = []

    with open('score_data.csv', 'r') as csvfile:
        data = csv.reader(csvfile)
        header = next(data)
        query = "INSERT INTO Assessment_Results (score, date_taken, time_taken, manager_id, person_id, competency_id, assessment_id) VALUES (?, ?, ?, ?, ?, ?, ?)"
        if header != None:

            for row in data:
                cursor.execute(query, row[1::])
                # data_list.append(row[0])
                # print(data_list)

        # cursor.executemany(query, [data_list, header, data])

        connection.commit()
# import_csv()