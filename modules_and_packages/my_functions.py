def my_sum(a, b):
    return a + b


def get_valid_integer():
    number = None
    while number is None:
        number = input('number = ')
        try:
            number = int(number)
        except ValueError:
            number = None
    return number


def dummy_function():
    pass
