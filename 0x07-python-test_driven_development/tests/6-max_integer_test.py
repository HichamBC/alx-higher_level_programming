#!/usr/bin/python3
"""Unittest for max_integer([..])
"""
import unittest
max_integer = __import__('6-max_integer').max_integer


class TestMaxInteger(unittest.TestCase):
    """
    unittest class for max_integer (inheritance)
    """
    def test_module_doc(self):
        """
        test for module docstring
        """
        mod = __import__("6-max_integer").__doc__
        self.assertTrue(len(mod) > 1)

    def test_function_doc(self):
        """
        test for function docstring
        """
        func = __import__("6-max_integer").max_integer.__doc__
        self.assertTrue(len(func) > 1)

    def test_empty_list(self):
        """
        test for empty list
        """
        self.assertIsNone(max_integer([]))

    def test_single_element(self):
        """
        test for a single element list
        """
        self.assertEqual(max_integer([5]), 5)

    def test_positive_numbers(self):
        """
        test for list of positive numbers
        """
        self.assertEqual(max_integer([20, 13, 45, 7, 50, 33]), 50)

    def test_negative_numbers(self):
        """
        test for list of negative numbers
        """
        self.assertEqual(max_integer([-20, -13, -45, -7, -50, -33]), -7)

    def test_mixed_numbers(self):
        """
        test for list of mixed numbers
        """
        self.assertEqual(max_integer([-20, 13, 45, -7, -50, 33]), 45)

    def test_float_numbers(self):
        """
        test for list of float numbers
        """
        self.assertEqual(max_integer([1.5, 2.7, 3.3, 4.6, 5.1]), 5.1)

    def test_duplicate_numbers(self):
        """
        test for list of duplicated numbers
        """
        self.assertEqual(max_integer([15, 20, 7, 15, 15, 7, 20, 20]), 20)

    def test_large_list(self):
        """
        test for large list
        """
        self.assertEqual(max_integer(list(range(1000000))), 999999)
