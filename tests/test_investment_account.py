"""Author : Om Patel
Date: 2024-10-4

To run : python -m unittest tests/test_investment_account.py
"""
import unittest
from datetime import date, timedelta
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
        self.assertEqual(0.50, round(account.get_service_charges(), 2))

    def test_service_charge_within_a_decade(self):
        account = InvestmentAccount(2004, 2904, 1000.0, date(2024, 10, 3), 2.55)
        self.assertEqual(account.get_service_charges(), 3.05)

    def test_string_method_for_more_than_a_decade(self):
        account = InvestmentAccount(2004, 2904, 1000.0, date(2013, 10, 5), 2.55)
        expected_str = (f"Account Number: 2004 "
                        f"Client Number: 2904 "
                        f"Balance: $1,000.00\n"
                        f"Date Created: {date.today() - timedelta(days=11 * 365.25)} "
                        f"Management Fee: Waived "
                        f"Account Type: Investment\n")
        self.assertEqual(str(account), expected_str)

    def test_string_method_within_a_decade(self):
        account = InvestmentAccount(2004, 2904, 1000.0, date(2024, 10, 4), 2.55) 
        expected_str = (f"Account Number: 2004 "
                        f"Client Number: 2904 "
                        f"Balance: $1,000.00\n"
                        f"Date Created: {date.today()} "
                        f"Management Fee: $2.55 "
                        f"Account Type: Investment")
        self.assertEqual(str(account).strip(), expected_str)

if __name__=='__main__':
    unittest.main()

