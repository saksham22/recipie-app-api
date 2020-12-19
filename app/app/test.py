from django.test import TestCase
from app.calc import add,minus

class CalcTests(TestCase):
    def test_add_number(self):
        """ Test that two number are added together"""
        self.assertEqual(add(3,8),11)
    def test_substract_numbers(self):
        """ Test that values are substracted and returned """
        self.assertEqual(minus(8,8),0)
