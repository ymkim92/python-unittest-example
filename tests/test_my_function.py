"""unittest"""

import unittest
from unittest import mock

from src.my_function import add, random


class MyFunctionTestCase(unittest.TestCase):
    """class for my function test"""

    def test_add(self):
        """test add"""
        self.assertEqual(add(1, 1), 2)
        self.assertTrue(add(1, 2) == 3)

    @mock.patch("os.urandom")
    def test_random(self, random_mock):
        """test random"""
        random_mock.return_value = "aaa"
        self.assertEqual(random(2), "2aaa")
