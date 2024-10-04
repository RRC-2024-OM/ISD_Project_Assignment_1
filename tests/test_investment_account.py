"""Author : Om Patel
Date: 2024-10-4

To run : python -m unittest tests/test_investment_account.py
"""
import unittest
from datetime import date
from bank_account.investment_account import InvestmentAccount

class TestInvestmentAccount(unittest.TestCase):

    def test_initialization_valid_numbers(self):
        account = InvestmentAccount(2004, 2904, 1000.0, date(2024, 10, 4), 2.55)
        self.assertEqual(account.account_number, 2004)
        self.assertEqual(account.client_number, 2904)
        self.assertEqual(account.balance, 1000.0)
        self.assertEqual(account._InvestmentAccount__management_fee, 2.55)

    def test_initialization_with_invalid_fee(self):
        account = InvestmentAccount(2004, 2904, 1000.0, date(2024, 10, 4), "Invalid fee" )
        self.assertEqual(account._InvestmentAccount__management_fee, 2.55)

    def test_service_charge_for_just_over_decade(self):
        account = InvestmentAccount(2004, 2904, 1000.0, date(2013, 10, 4), 2.55)
        self.assertEqual(account.get_service_charges(), 0.50)

    def test_service_charge_for_a_decade(self):
        account = InvestmentAccount(2004, 2904, 1000.0, date(2014, 10, 4), 2.55)
        self.assertEqual(account.get_service_charges(), 3.05)

    def test_service_charge_within_a_decade(self):
        account = InvestmentAccount(2004, 2904, 1000.0, date(2024, 10, 3), 2.55)
        self.assertEqual(account.get_service_charges(), 3.05)

if __name__=='__main__':
    unittest.main()

