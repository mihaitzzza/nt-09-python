from algorithm import gcd as get_gcd, lcm as get_lcm


class Fraction:
    def __init__(self, numerator, denominator):
        if type(numerator) != int:
            raise ValueError('Numerator should be an integer.')

        if type(denominator) != int:
            raise ValueError('Denominator should be an integer.')

        if denominator == 0:
            raise ValueError('Denominator cannot be 0.')

        gcd = get_gcd(abs(numerator), abs(denominator))

        self.numerator = numerator // gcd
        self.denominator = denominator // gcd

    def __add__(self, other):
        lcm = get_lcm(self.denominator, other.denominator)
        self_multiply_by = lcm // self.denominator
        other_multiply_by = lcm // other.denominator

        new_numerator = self.numerator * self_multiply_by + other.numerator * other_multiply_by

        return Fraction(new_numerator, lcm)

    def __sub__(self, other):
        lcm = get_lcm(self.denominator, other.denominator)
        self_multiply_by = lcm // self.denominator
        other_multiply_by = lcm // other.denominator

        new_numerator = self.numerator * self_multiply_by - other.numerator * other_multiply_by

        return Fraction(new_numerator, lcm)

    def self_inverse(self):
        aux = self.numerator
        self.numerator = self.denominator
        self.denominator = aux

    def inverse(self):
        return Fraction(self.denominator, self.numerator)

    def __str__(self):
        return f'{self.numerator}/{self.denominator}'


print('fraction module: ', __name__)
if __name__ == '__main__':
    fraction_1 = Fraction(5, 18)
    fraction_2 = Fraction(2, 3)
    fraction_3 = fraction_1 + fraction_2  # 51/54
    fraction_4 = fraction_1 - fraction_2  # 5/18 - 12/18 = -7/18
    fraction_5 = fraction_1.inverse()  # inverse of `fraction_1` 5/18 => 18/5

    print(f'1 = {fraction_1}')
    print(f'2 = {fraction_2}')
    print(f'3 = {fraction_3}')
    print(f'4 = {fraction_4}')
    print(f'5 = {fraction_5}')

    print('\n' * 10)
    print('fraction_2', fraction_2)
    fraction_2.self_inverse()
    print('fraction_2', fraction_2)
