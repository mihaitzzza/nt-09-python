# from functools import reduce

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

# print('students', students)


# def sort_by_grade(student):
#     return student['grade']
# sort_by_grade = lambda student: student['grade']  # do not use lambda functions this way
# print(id(sort_by_grade))

# def sort_by_last_name(student):
#     return student['last_name']
# sort_by_last_name = lambda student: student['last_name']  # do not use lambda functions this way
# print(id(sort_by_last_name))

# students.sort(key=sort_by_grade, reverse=True)
# print('students', students)

# sorted_students_by_grade = sorted(students, key=lambda student: student['grade'])
# print('students', students)
# print('sorted_students_by_grade', sorted_students_by_grade)
#
# sorted_students_by_last_name = sorted(students, key=lambda student: student['last_name'])
# print('sorted_students_by_last_name', sorted_students_by_last_name)

# a = lambda x: x
# b = lambda x, y: x + y
# print(id(a), a(12))
# print(id(b), b(2, 3))

# print(id(lambda x, y: x + y))
# print(id(lambda x, y: x + y))

# print((lambda x: f'{x} is an even number.' if x % 2 == 0 else f'{x} is an odd number.')(13))
# a = True if 13 % 2 == 0 else False
# print('a', a)
# a = 12 % 2 == 0
# if 12 % 2 == 0:
#     a = True
# else:
#     a = False

# def get_updated_student(student):
#     new_student = student.copy()
#     grade_int = int(student['grade'])
#     new_student['grade_int'] = grade_int
#     new_student['grade_decimals'] = float(student['grade']) - grade_int
#     return new_student
#
#
# # updated_list = []
# # for student in students:
# #     updated_list.append(get_updated_student(student))
# updated_list = list(map(get_updated_student, students))
# print('updated_list', updated_list)


# my_list = [1, 2, 3, 4, 5, 6, 7, 8]
# #          0  1  0  1  0  1  0  1
# number_parity = list(map(lambda number: int(number % 2 == 0), my_list))
# print('number_parity', number_parity)

# def is_student_promoted(item):
#     return item['grade'] >= 5.00


# promoted_students = []
# for student in students:
#     if is_student_promoted(student):
#         promoted_students.append(student)

# promoted_students = list(filter(lambda item: item['grade'] >= 5.00, students))
# print('promoted_students', promoted_students)

# def get_updated_student(student):
#     new_student = student.copy()
#     grade_int = int(student['grade'])
#     new_student['grade_int'] = grade_int
#     new_student['grade_decimals'] = float(student['grade']) - grade_int
#     return new_student


# updated_students = list(map(get_updated_student, students))
# promoted_students = list(filter(lambda item: item['grade'] >= 5.00, updated_students))
# print('promoted_students', promoted_students)

# promoted_students = list(filter(lambda item: item['grade'] >= 5.00, students))
# updated_students = list(map(get_updated_student, promoted_students))
# print('promoted_students', promoted_students)

def get_updated_student(student):
    new_student = student.copy()
    grade_int = int(student['grade'])
    new_student['grade_int'] = grade_int
    new_student['grade_decimals'] = float(student['grade']) - grade_int
    return new_student


# def test(accumulator, current_item):
#     print(accumulator, current_item)
#
#     if type(accumulator) == dict:  # accumulator is first item in the list
#         updated_accumulator = []
#         if accumulator['grade'] >= 5.00:
#             updated_accumulator.append(get_updated_student(accumulator))
#     else:
#         updated_accumulator = accumulator[:]
#
#     if current_item['grade'] >= 5.00:
#         updated_accumulator.append(get_updated_student(current_item))
#
#     return updated_accumulator
#
#
# promoted_students = reduce(test, students)
# print('promoted_students', promoted_students)

# order = [4, 1, 3, 2]
# # zip_example = list(zip(['s1', 's2', 's3', 's4'], order, ['a', 'b', 'c', 'd', 'e']))
# promoted_students = filter(lambda item: item['grade'] >= 5.00, students)
# updated_students = map(get_updated_student, promoted_students)
# students_with_order = zip(updated_students, order)
# for student, index in students_with_order:
#     print(f'Student {student["last_name"]} {student["first_name"]} has order = {index}')
#
# x = dict(zip([1, 2, 3], ['a', 'b', 'c']))
# print(x)


# l = list(range(10))
# print('l', l)

# l2 = list(map(lambda x: x ** 2, l))
# print('l2', l2)

# l2 = [number ** 2 if number % 2 == 0 else number for number in l]
# print('l2', l2)

# promoted_students = [student['last_name'] + ' ' + student['first_name'] for student in students if student['grade'] >= 5.00]
# print('promoted_students', promoted_students)

keys = ['a', 'b', 'c']  # {'a': 0, 'b': 1, 'c': 2}
values = 1, 2, 3
# x1 = dict(zip(keys, values))
# print('x1', x1)

# x2 = {key: value for key, value in zip(keys, values)}
# print('x2', x2)

x3 = {value: index for index, value in enumerate(keys)}
print('x3', x3)
