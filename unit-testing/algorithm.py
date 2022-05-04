# def gcd(a, b):
#     while a % b != 0:
#         a = b % a
#         b = a
#
#     return b
def gcd(a, b):
    if a == 0:
        return b

    return gcd(b % a, a)


def lcm(a, b):
    _gcd = gcd(a, b)
    return (a // _gcd) * b
