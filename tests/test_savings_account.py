"""Author : Om Patel
Date : 2024-10-05

To run : python -m unittest tests/test_savings_account.py
"""
import unittest
from datetime import date
from bank_account.savings_account import SavingsAccount

class TestSavingsAccount(unittest.TestCase):

    def test_initialization_valid_number(self):
        account = SavingsAccount(2004, 2904, 1000.00, date.today(), 50.0)
        self.assertEqual(account.account_number, 2004)
        self.assertEqual(account.client_number, 2904)
        self.assertEqual(account.balance, 1000.00)
        self.assertEqual(account._SavingsAccount__minimum_balance, 50.0)

    def test_initialization_invalid_minimum_balance_numbers(self):
        account = SavingsAccount(2004, 2904, 1000.00, date.today(), "Invalid")
        self.assertEqual(account._SavingsAccount__minimum_balance, 50.0)
        

if __name__ == '__main__':
    unittest.main()