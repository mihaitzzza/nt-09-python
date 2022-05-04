from parameterized import parameterized
from fraction import Fraction


@parameterized.expand([
    (200, 400, '1/2'),
    (125, 375, '1/3'),
])
def test_fraction_init(numerator, denominator, expected_result):
    result = Fraction(numerator, denominator)
    assert str(result) == expected_result
