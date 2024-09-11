"""
Description: Unit tests for the Client class.
Author: ACE Faculty
Modified by: Om Patel
Date: 2024-09-11
Usage: To execute all tests in the terminal execute
the following command:
    python -m unittest tests/test_client.py
"""
import unittest
from client.client import Client
from email_validator import EmailNotValidError

class Test_Client(unittest.TestCase):
    """Tests for the Client class.
    """

    def setUp(self):
        """Setup runs AUTOMATICALLY before each test method and
        provides initial values for the class attributes.
        """
        self.client = Client(1010, "Om", "Patel", "ompatel@gmail.com")

    def test_init_initializes_object(self):
        self.assertEqual(self.client._Client__client_number, 1010)
        self.assertEqual(self.client._Client__first_name, "Om")
        self.assertEqual(self.client._Client__last_name, "Patel")
        self.assertEqual(self.client._Client__email_address, "ompatel@gmail.com")

    def test_init_non_numeric_client_id_raise_exception(self):
        with self.assertRaises(ValueError) as context:
            Client("abc", "Om", "Patel", "ompatel@gmail.com")
        self.assertEqual("Client number should be numeric.", str(context.exception))

    def test_init_blank_first_name_blank(self):
        with self.assertRaises(ValueError) as context:
            Client(1010, " ", "Patel", "ompatel@gmail.com")
        self.assertEqual("First name cannot be blank.", str(context.exception))

    def test_init_last_name_blank(self):
        with self.assertRaises(ValueError) as context:
            Client(1010, "Om", " ", "ompatel@gmail.com")
        self.assertEqual("Last name cannot be blank.", str(context.exception))

    def test_init_invalid_email(self):
        client = Client(1010, "Om", "Patel", "invalid_email")
        self.assertEqual(client.email_address, "email@pixell-river.com")

    def test_client_number_accessor_returns_correct_state(self):
        self.assertEqual(self.client.client_number, 1010)

    def test_first_name_accessor_returns_correct_state(self):
        self.assertEqual(self.client.first_name, "Om")

    def test_last_name_accessor_returns_correct_state(self):
        self.assertEqual(self.client.last_name, "Patel")

    def test_email_address_accessor_returns_correct_state(self):
        self.assertEqual(self.client.email_address, "ompatel@gmail.com")

    def test_str_returns(self):
        expected = (f"Name: Patel, Om\n"
                    f"Client Number: 1010\n"
                    f"Email Address: ompatel@gmail.com\n")

        self.assertEqual(expected, str(self.client))


if __name__ == '__main__':
    unittest.main()
