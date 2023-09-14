import unittest
from unittest import TestCase
from price_discount import discount


class TestDiscount(TestCase):

    def test_list_of_three_prices(self):
        prices = [10, 4, 20]
        expected_discount = 4
        self.assertEqual(expected_discount, discount(prices))

    def test_of_two_prices(self):
        prices = [20, 3]
        expected_discount = 3
        self.assertEqual(expected_discount,discount(prices))

    def test_list_of_four_prices(self):
        prices = [15, 5, 4, 10]
        expected_discount = 4
        self.assertEqual(expected_discount,discount(prices))

    def test_of_five_prices(self):
        prices = [15, 10, 12, 11, 13]
        expected_discount = 10
        self.assertEqual(expected_discount,discount(prices))

    def test_of_float(self):
        prices = [12.3, 11, 1]
        expected_discount = 1
        self.assertEqual(expected_discount,discount(prices))
    # TODO more unit tests here. Each test should test one scenario


if __name__ == '__main__':
    unittest.main()
