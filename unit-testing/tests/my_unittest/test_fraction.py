import unittest
from parameterized import parameterized
from fraction import Fraction


class FractionTestCase(unittest.TestCase):
    @parameterized.expand([
        (100, 200, '1/2'),
        (3, 18, '1/6'),
    ])
    def test_fraction_is_simplified(self, numerator, denominator, expected_result):
        result = Fraction(numerator, denominator)
        self.assertEqual(expected_result, str(result))
