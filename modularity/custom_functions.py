# # # # def my_function():
# # # #     print('Message from my function.')
# # # #
# # # #
# # # # my_function()
# # # # print('END OF PROGRAM!')
# # #
# # # # def my_sum(a, b):
# # # #     print('Sum of numbers =', a + b)
# # # #
# # # #
# # # # x = 20
# # # # y = 23
# # # # my_sum(x, y)  # my_sum(20, 23)
# # #
# # # # def my_sum(a, b):
# # # #     return a + b
# # # #
# # # #
# # # # returned_value = my_sum(12, 7)
# # # # print('Sum of numbers =', returned_value)
# # #
# # # def s(a, b, c=100, d=200):
# # #     print(a, b, c, d)
# # #
# # #
# # # # s(10, 7, d=-20)
# # # s(a=7, b=10, d=-20)
# #
# # # def my_function(*args, **kwargs):
# # #     print('my_function', args, kwargs)
# # #
# # #
# # # my_function()
# # # my_function(1, 2)
# # # my_function(1, 2, c=3, d=4)
# # # my_function([1, 2, 3], ('a', 'b', 'c'), another_key=set([True, False, None]))
# #
# # # def my_function(param_1, param_2, *args, keyword_1=None, keyword_2=None, **kwargs):
# # #     print(param_1, param_2, args, keyword_1, keyword_2, kwargs)
# # #
# # # my_function(1, 2, 'a', keyword_1='abc', keyword_3="this goes to kwargs")
# #
# # # def f(a, b, c, *args, a1, b1, c1, **kwargs):
# # #     print(a, b, c, args, a1, b1, c1, kwargs)
# # #
# # #
# # # f(*{1, 2, 3, 4, 5, 6}, **{'a1': 1, 'b1': 2, 'c1': 3, 'd1': 4})
# #
# # # a = [1, 2, 3]
# # #
# # #
# # # def f(my_list=[]):
# # #     my_list.append(4)
# # #
# # #
# # # print(a)
# # # f(a)
# # # print(a)
# #
# # def s(n):
# #     if n == 0:
# #         return 0
# #
# #     return n + s(n - 1)
# #
# #
# # # result = s(5)  # 0 + 1 + 2 + 3 + 4 + 5 = 15
# # # print('sum of 5:', result)
# # # raise NameError('THis is my custom message for Name Error! Catch me if you can!')
# #
# # # user_input = input('give me your message: ')
# # # try:
# # #     user_input = int(user_input)
# # #     user_input = 'abc'
# # #     result = s(user_input)
# # #     print(f'sum of numbers from 0 to {user_input} = {result}.')
# # # except ValueError as e:
# # #     print(f"Caught ValueError exception: {e}")
# # # except TypeError as e:
# # #     print(f"Caught TypeError exception: {e}")
# # # else:
# # #     print('The code in try was successful.')
# # # finally:
# # #     print('I am available no matter what.')
# #
# # try_number = 1
# # while True:
# #     if try_number > 3:
# #         break
# #     elif try_number > 1:
# #         print(f'You have {3 - try_number + 1} tries.')
# #
# #     user_input = input('give me your message: ')
# #     try:
# #         user_input = int(user_input)
# #     except ValueError:
# #         print(f'"{user_input}" is not a valid integer.')
# #         try_number += 1
# #     else:
# #         break
# #     finally:
# #         print(f'Your input is {user_input}.')
# #
# # if try_number > 3:
# #     print('You was not able to provide a valid integer. Sorry!')
# # else:
# #     result = s(user_input)
# #     print(f'sum of numbers from 0 to {user_input} = {result}.')
#
# print(dir(__builtins__))

a = 10


def outer_function():
    def inner_function():
        # a = [1, 2, 3]
        print('inner', a)

    # a = 'abc'
    # global a
    # a = 'abc'
    inner_function()
    print('outer', a)


outer_function()
print('global', a)
