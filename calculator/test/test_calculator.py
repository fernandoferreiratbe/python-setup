# _*_ encoding: utf-8 _*_

import unittest
from calculator.calculator import Calculator


class TestCalculator(unittest.TestCase):

    def setUp(self):
        self.calculator = Calculator()

    def test_add_given_two_values_should_return_the_correct_value(self):
        result = self.calculator.add(10, 10)

        self.assertEqual(first=result, second=20, msg='Invalid sum operation performed.')

    def test_subtract_given_two_values_should_return_the_correct_value(self):
        result = self.calculator.subtract(10, 10)

        self.assertEqual(first=result, second=0, msg='Invalid subtract operation performed.')

    def test_multiply_given_two_values_should_return_the_correct_value(self):
        result = self.calculator.multiply(10, 10)

        self.assertEqual(first=result, second=100, msg='Invalid multiply operation performed.')

    def test_divide_given_two_values_should_return_the_correct_value(self):
        result = self.calculator.divide(10, 10)

        self.assertEqual(first=result, second=1, msg='Invalid divide operation performed.')

