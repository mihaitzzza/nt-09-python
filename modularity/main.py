# #age = 2
#
# # if age >= 18:
# #     print('1. You can taste a beer! Congrats.')
# # elif age >= 12:
# #     print('2. You can taste a Coca-Cola! Not bad.')
# # elif age >= 6:
# #     print('3. Some random text.')
# # else:
# #     print('4. Go have some milk ;)')
#
# # if age >= 18:
# #     print('1. You can taste a beer! Congrats.')
# # elif age >= 6:
# #     print('age is between [6, 12]')
# #     if age >= 12:
# #         print('2. You can taste a Coca-Cola! Not bad.')
# #     else:
# #         print('3. Some random text.')
# # else:
# #     print('4. Go have some milk ;)')
#
#
# # if age >= 18:
# #     pass
# # else:
# #     print('Persoana minora.')
# # if age < 18:
# #     print('Persoana minora.')
# #
# # print('END OF PROGRAM!')
#
# # age = 20
# #
# # while condition is True:
# #     print('Do something')
# # while age >= 18:
# #     print('Duplicate message')
#
# # print(range(10), list(range(10)))
# # print(range(5, 10), list(range(5, 10)))
# # print(range(5, 10, 2), list(range(5, 10, 2)))
#
# # for element in sequence:
# #     # print('Do something')
# # for number in range(10):
# #     print(f'{number + 1}. Duplicate message')
#
# # my_dict = {"a": 1, "b": 2}
# # for key in my_dict:
# #     print(key, my_dict[key])
#
# # for x in "ana are mere":
# #     print(x)
#
# # while True:
# #     print('Duplicate message.')
# #     continue
# #     # break
#
# # for item in range(10):
# #     if item >= 5:
# #         break
# #
# #     if item % 2 == 1:
# #         continue
# #
# #     print(item, 'Even number found!')
#
# # sequence = range(10)
# # number = 0
# # while number <= 9:
# #     print(f'{number + 1}. Duplicate message')
# #     number += 1
# # my_dict = {"a": 1, "b": 2}
# # keys = list(my_dict.keys())
# # index = 0
# # while index < len(keys):
# #     print(keys[index], my_dict[keys[index]])
# #     index += 1
#
# print('END OF PROGRAM!')

my_abc = ['a', 'b', 'c', 'd', 'e']  # len(my_abc)
# for item in my_abc:
#     print(item)
# for index in range(len(my_abc)):
#     print(index, my_abc[index])
# for index, item in enumerate(my_abc):
#     print(index, item)
# print(enumerate(my_abc), type(enumerate(my_abc)), tuple(enumerate(my_abc)))

# a, b, c = 1, 2, 3
# print(a)
# print(b)
# print(c)
# for a, b, c, d in [(1, 2, 3, 4), ('a', 'b', 'c', 'd'), (None, True, 'a', 2)]:
#     print(a, b, c, d)

# my_list = ['a', 'b', 'c']
# for index, ch in enumerate(my_list[1:]):
#     print(index + 2, ch)

print(tuple(zip([1, 2, 3], ['a', 'b', 'c'])))
my_list = ['a', 'b', 'c']  # 8. a, 10. b, 12. c
for i, ch in zip(range(8, len(my_list) + 8 + 2, 2), my_list):
    print(i, ch)


print(tuple(zip([1, 2, 3, 4, 5], ['a', 'b', 'c'])))
