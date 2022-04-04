import os
import csv
import json

students = [
    {
        'first_name': 'Dan',
        'last_name': 'Popescu',
        'grade': 7.25  # => "grade_int": 7, "grade_decimals": 0.25
    },
    {
        'first_name': 'Vio',
        'last_name': 'Ionescu',
        'grade': 3.75
    },
    {
        'first_name': 'George',
        'last_name': 'Popescu',
        'grade': 8.25
    },
    {
        'first_name': 'Grigore',
        'last_name': 'Ionescu',
        'grade': 9.00
    },
]

# with open('file_examples/students.txt', 'w') as my_file:
#     for student in students:
#         my_file.write(student['last_name'] + ' ' + student['first_name'] + '\n')

# with open(os.path.join('file_examples', 'students.txt')) as my_file:
#     print(my_file.read().split('\n'))

# with open('file_examples/students.csv', 'w') as my_file:
#     writer = csv.writer(my_file)
#     keys = students[0].keys()
#     writer.writerow(keys)
#     for student in students:
#         writer.writerow(student.values())


# students_from_file = []
# with open('file_examples/students.csv') as csv_file:
#     reader = csv.reader(csv_file)
#
#     for index, row in enumerate(reader):
#         if index == 0:
#             keys = row
#         else:
#             students_from_file.append(dict(zip(keys, row)))
#
# print('students_from_file', students_from_file)

# with open('file_examples/students.json', 'w') as json_file:
#     json.dump(students, json_file, indent=2)

# with open('file_examples/students.json') as json_file:
#     students_from_file = json.load(json_file)
#
# print('students_from_file', students_from_file)
