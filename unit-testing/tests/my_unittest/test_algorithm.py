import unittest
from algorithm import gcd as get_gcd, lcm as get_lcm


class AlgorithmTestCase(unittest.TestCase):
    def test_gcd(self):
        result = get_gcd(6, 20)  # 2
        self.assertEqual(2, result)

    def test_lcm(self):
        result = get_lcm(3, 18)  # 18
        self.assertEqual(18, result)
