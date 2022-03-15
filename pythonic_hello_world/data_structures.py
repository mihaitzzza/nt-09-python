# my_age = 12
# my_string = 'random string'
# my_list = [my_age, my_string, True, None, 3+2j]  # length = 5
# #            0          1       2    3     4
# #           -5         -4      -3   -2    -1
# print('my_list', my_list, type(my_list))
# print('first element:', my_list[0], type(my_list[0]), my_list[-5])
# print('second element:', my_list[1], type(my_list[1]), my_list[-4])
# print('third element:', my_list[2], type(my_list[2]), my_list[-3])
# print('fourth element:', my_list[3], type(my_list[3]), my_list[-2])
# print('fifth element:', my_list[4], type(my_list[4]), my_list[-1])

# my_list = []
# print(my_list[2])  # IndexError: list index out of range

# my_age = 12
# my_string = 'random string'
# my_list = [my_age, my_string, True, None, 3+2j, 'a', 'b', 'c', 'd']  # length = 9
# print('list length =', len(my_list))
# print(my_list[len(my_list) - 2])
# slice: my_list[start:end:step]
# print(my_list[1:])
# print(my_list[:-1])  # print(my_list[:len(my_list)-1])
# print(my_list[::2])
# print(my_list[1::2])
# print(my_list[:-1:2])
# print(my_list[::-1])  #print(my_list[-1: 0: -1])
# a = my_list[::-1]
# print(id(my_list), id(a))

# my_list = [1, 2, 3, 4, 4, 4, 5]
# print(my_list.count(4))

# a = 2
# my_list = [1, a, 3]
# print('my_list', my_list, a)
# a = 4
# print('my_list', my_list, a)

# my_list = [1, 2, 3]
# my_second_list = my_list[::-1]
# print('my_list', my_list)
# print('my_second_list', my_second_list)
# my_list = [1, 2, 3]
# my_list.reverse()
# print('my_list', my_list)
# a = [1, 2, 3] + [4, 5, 6]
# print(a)
# a[3] = 20
# print(a)
# a.append(21)
# print(a)

# my_tuple = ()  # my_tuple = tuple()
# my_tuple = (1, 2, 3, 'a', 'b', 'c', True, False)
# print(my_tuple, type(my_tuple))
# print(my_tuple[0], my_tuple[-1], len(my_tuple))
# my_tuple[3] = 20  # TypeError: 'tuple' object does not support item assignment

# my_list = [1, 2, 3]
# print('my_list', my_list, type(my_list))
# my_tuple = tuple(my_list)
# print('my_tuple', my_tuple, type(my_tuple))
# my_other_list = list(my_tuple)
# print('my_other_list', my_other_list, type(my_other_list))
# print(my_list == my_other_list)
# print(my_list is my_other_list)

# a = [1, 2, 3]
# b = a
# # print(a is b)
# print('a', a)
# print('b', b)
# a = [1, 2, 3]
# a.append(4)  # a ==> [1, 2, 3, 4]
# print('a', a)
# print('b', b)

# my_list = [1, 2, 3]
# print('my_list', my_list, type(my_list))
# my_tuple = tuple(my_list)
# print('my_tuple', my_tuple, type(my_tuple))
# my_other_list = list(my_tuple)
# print('my_other_list', my_other_list, type(my_other_list))
# print(my_list == my_other_list)
# print(my_list is my_other_list)

# my_tuple = (1, 2, 3)
# id_1 = id(my_tuple)
# l = list(my_tuple)
# l.append(4)
# my_tuple = tuple(l)
# id_2 = id(my_tuple)
# # print('my_tuple', my_tuple)
# print(id_1, id_2)

# my_tuple = 1, 2, 3
# print('my_tuple', my_tuple, type(my_tuple))
#
# a, b, c = 1, 'c', None
# print(a, b, c)

# my_dict = {}
# print('my_dict', my_dict, type(my_dict))
# my_dict = {
#     "key1": 10,
#     "key2": "abc",
#     1: 'abc',
#     (3 + 2j): True,
#     (1, 2, 3): "abc",
#     "abc": "abc",
#     "existing_key": 1250,
#     23: 100
# }
# print(my_dict)
# my_dict[3 + 2j] = [1, 2, 3]
# my_dict["new_key"] = {"a": 1, "b": 2, "c": 2}
# # print(my_dict["key2"], my_dict[3+2j])
# print(my_dict['new_key'])
# # print(my_dict['not_existing_key'])  # IndexError: list index out of range
# # print('not_existing_key', my_dict.get('not_existing_key'))  # None
# print('existing_key', my_dict.get('existing_key', 100))  # 200
# print('not_existing_key', my_dict.get('not_existing_key', 100))  # 100
# print(my_dict[23])
#
# student_1 = {
#     "first_name": "Mihai",
#     "last_name": "Popescu",
#     "age": 23,
#     "city": "Craiova"
# }
# student_2 = {
#     "first_name": "Gigle",
#     "last_name": "Popescu",
#     "age": 10,
#     "city": "Iasi",
#     "grade": {
#         "math": [{
#             "date": "2022-03-15",
#             "value": 7
#         }, {
#             "date": "2022-03-13",
#             "value": 10.00
#         }],
#         "biology": [2, 3],
#     }
# }
# students = [student_1, student_2]
# print('students', students)
# students[0]["last_name"] = "Vladu"
# print('students', students)
#
# student_3 = {**student_1, **student_2}
# # student_3 = {"student_1": student_1, "student_2": student_2}
# print('student_3', student_3, type(student_3))

# a = {"a": 2, "b": 3, "c": 4}
# b = {"b": 2, "c": 2, "d": 2}
# print({**a, **b})

# a = {
#     "key1": {
#         "key1.1": 1,
#         "key1.2": 2
#     },
#     "key2": (1, 2)
# }
# b, c = a["key2"]
# print('b', b)
# print('c', c)

# a = {
#     "nume_1": {
#         "key1": 1,
#         "key2": 2,
#     },
#     "nume_2": {
#         "key1": 3,
#         "key2": 4
#     },
# }
#
# print('a', a)

# my_dict = {"a": 2}
# del my_dict["a"]
# print('my_dict', my_dict)
# print(my_dict["a"])

# my_list = [1, 2, 3, 4, 5]
# my_tuple = (1, 2, 3, 4, 5)
# print(10 in my_list)
# print(10 not in my_list)
# print(not (10 in my_list))  # print(10 not in my_list)
# print(2 < 3 and 5 > 4)
# print(not(2 < 3 and 5 > 4))  # print(2 >= 3 or 5 <= 4)

# my_dict = {"key1": 1, "key2": 2}
# print("key1" in my_dict, "key3" in my_dict)
# print('my_dict.keys()', my_dict.keys())
# print('my_dict.values()', my_dict.values())
# print(2 in my_dict.values())
# print('my_dict.items()', my_dict.items())


# my_dict = {"key1": 1, "key2": 1}
# print(my_dict.values())

# my_set = set()
# my_set = {1, 0, 2, 3, 'a', 'bca', None, True, False, 3, 3, 3, 3, 3}
# print('my_set', my_set, type(my_set))
# print(my_set[2])  # TypeError: 'set' object is not subscriptable
# print(my_set)
# print(bool(1), bool(0), bool(''), bool("a"), bool([]), bool([0]), bool([""]), bool(20), bool(-7))
# print(not 1, not 0)

# my_list = [1, 2, 3, 4, 4, 5]
# my_set = set(my_list)  # {1, 2, 3, 4, 5}
# print(my_list)
# print(my_set)
# print(len(my_list) == len(my_set))


# my_set = {1, 2, 3}
# my_set.add(4)
# print(my_set)

# a = {1, 2, 3}
# b = a
# a.add(4)
# print(a, b)
# print(a is b)


