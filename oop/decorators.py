# # def my_sum(a, b):
# #     return a + b
# #
# #
# # def wrapper_function(my_function, a, b):
# #     return my_function(a, b)
# #
# #
# # def returned_function():
# #     return my_sum
# #
# #
# # my_var = my_sum
# # print(my_var(2, 8))
# # print(wrapper_function(my_sum, 2, 10))
# # print(returned_function()(6, 7))
#
#
# # def my_decorator(my_function):
# #     def wrapper(a, b):
# #         print(f'{a} is {"even" if a % 2 == 0 else "odd"} & {b} is {"even" if b % 2 == 0 else "odd"}')
# #         return my_function(a, b)
# #
# #     return wrapper
# #
# #
# # def my_sum(a, b):
# #     return a + b
#
#
# # my_decorated_function = my_decorator(my_sum)
# # result = my_decorated_function(2, 7)
# # print('result', result)
#
# # my_decorated_function = my_decorator(my_sum)
# #
# # result_with_prints = my_decorated_function(2, 7)
# # print('result_with_prints', result_with_prints)
# #
# # print('\n')
# #
# # result_without_prints = my_sum(12, 43)
# # print('result_without_prints', result_without_prints)
#
#
# # def my_decorator(my_function):
# #     def wrapper(a, b):
# #         print(f'{a} is {"even" if a % 2 == 0 else "odd"} & {b} is {"even" if b % 2 == 0 else "odd"}')
# #         result = my_function(a, b)
# #         print('show this message after the function is done!')
# #         return result
# #
# #     return wrapper
# #
# #
# # @my_decorator
# # def my_sum(a, b):
# #     return a + b
# #
# #
# # print(my_sum(2, 7))
#
# # def my_decorator_with_params(my_number):
# #     def my_decorator(my_function):
# #         def wrapper(a, b):
# #             result = my_function(a, b)
# #             return result ** my_number
# #
# #         return wrapper
# #
# #     return my_decorator
# #
# #
# # # def my_sum(a, b):
# # #     return a + b
#
#
# # # my_decorator = my_decorator_with_params(3)
# # # my_decorated_function = my_decorator(my_sum)
# # # result = my_decorated_function(2, 7)
# # result = my_decorator_with_params(2)(my_sum)(2, 7)
# # print('result', result)
#
#
# def my_decorator_with_params(my_number):
#     def my_decorator(my_function):
#         def wrapper(a, b):
#             result = my_function(a, b)
#             return result ** my_number
#
#         return wrapper
#
#     return my_decorator
#
#
# @my_decorator_with_params(2)
# def my_sum(a, b):
#     return a + b
#
#
# print(my_sum(2, 7))
