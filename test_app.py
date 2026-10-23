import unittest
from app import greet

class TestGreet(unittest.TestCase):
    def test_greet_returns_expected_message(self):
        self.assertEqual(
            greet("Ravi"),
            "Hello, Ravi! Welcome to the AWS Developer Tools demo."
        )

if __name__ == "__main__":
    unittest.main()