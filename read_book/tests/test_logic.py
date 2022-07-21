from unittest import TestCase

from read_book.logic import operations


class LogicTestCase(TestCase):
    def test_plus(self):
        result = operations(6, 13, '+')
        self.assertEqual(19, result)

    def test_minus(self):
        result = operations(10, 3, '-')
        self.assertEqual(7, result)

    def test_multiply(self):
        result = operations(2, 5, '*')
        self.assertEqual(10, result)
