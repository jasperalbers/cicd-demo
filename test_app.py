# test_app.py
import unittest
from app import add_numbers


class TestAddNumbers(unittest.TestCase):
    def test_addition(self):
        self.assertEqual(add_numbers(2, 2), 4)


if __name__ == "__main__":
    unittest.main()
