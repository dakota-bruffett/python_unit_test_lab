import unittest 
from unittest import TestCase
from price_discount import discount  

class TestDiscount(TestCase):

    def test_list_of_three_prices(self):
        prices = [10, 4, 20]
        expected_discount = 4
        self.assertEqual(expected_discount, discount(prices))


    def test_of_two_products(self):
        prices = [20, 3]
        expected_discount = 3
        self.assertEqual(expected_discount, discount(prices))

    def

    # TODO more unit tests here. Each test should test one scenario


if __name__ == '__main__':
    unittest.main()