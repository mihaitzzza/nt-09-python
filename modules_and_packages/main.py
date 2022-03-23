# import my_functions
# import my_package.helpers as h
import outer_package.my_package.constants as c
from my_functions import *
# from my_package.helpers import *
# from outer_package.my_package.helpers import print_greeting_message
from outer_package import print_greeting_message
from my_functions import my_sum

if __name__ == '__main__':
    print_greeting_message(c.GREETING_MESSAGE)  # h.print_greeting_message(c.GREETING_MESSAGE)

    a = get_valid_integer()  # a = my_functions.get_valid_integer()
    b = get_valid_integer()  # b = my_functions.get_valid_integer()
    result = my_sum(a, b)  # result = my_functions.my_sum(a, b)

    print(f'{a} + {b} = {result}')
