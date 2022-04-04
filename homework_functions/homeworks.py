# # # n = 10
# # #
# # #
# # # def rec_function(n):
# # #     if n == 0:
# # #         return 0
# # #
# # #     return n + rec_function(n - 1)
# # #
# # #
# # # print('sum of all numbers = ', rec_function(n))
# #
# # # def f():
# # #     return 2, 4, 5
# # #
# # #
# # # result = f()
# # # print(result, type(result))
# # # sum_all_numbers, sum_even_numbers, sum_odd_numbers = f()
# #
# # n = 10
# #
# #
# # def rec_function(n):
# #     if n == 0:
# #         return 0, 0, 0
# #
# #     prev_total, prev_even, prev_odd = rec_function(n - 1)
# #     total = n + prev_total
# #     if n % 2 == 0:
# #         even = prev_even + n
# #         odd = prev_odd
# #     else:
# #         even = prev_even
# #         odd = prev_odd + n
# #
# #     return total, even, odd
# #
# #
# # total_sum, even_sum, odd_sum = rec_function(n)
# # print('total =', total_sum)
# # print('even_sum =', even_sum)
# # print('odd_sum =', odd_sum)
#
# n = 10
# s = 0
#
#
# # if type(n) == int:
# #     s += n
# # elif type(n) == float:
# #     s += n
# # if type(n) == int or type(n) == float:
# #     pass
# #
# # if type(n) in [int, float]:
# #     pass
#
# # my_var = '55025'
# # print(my_var.isdigit())
#
# # def f(*args, **kwargs):
# #     s = 0
# #
# #     for i in args + tuple(kwargs.values()):
# #         if type(i) in [int, float]:
# #             s += i
# #     # for i in kwargs.values():
# #     #     if type(i) in [int, float]:
# #     #         s += i
# #
# #     return s
#
# def f(*args, **kwargs):
#     s = 0
#
#     for i in args + tuple(kwargs.values()):
#         try:
#             nr = int(i)
#             s += nr
#         except:
#             try:
#                 nr = float(i)
#                 s += nr
#             except:
#                 pass
#
#     return s
#
#
# case_1 = f(1, 5, -3, "abc", [12, 56, "cad"])
#
# case_2 = f()
# # print(case_2)
#
# case_3 = f(2, 4, "abc", param_1=2)
# # print(case_3)

l = [7, 8, 9, 2, 3, 1, 4, 10, 5, 6]

l.sort()
print(l)

l.sort(reverse=True)
print(l)

print(l[::2])
print(l[1::2])
print(l[1::3])

# l.sort()
# print(l[::2])
# print(l[1::2])
# print(l[2::3])


