"""Author : Om Patel
Date : 2024-10-03

Description : Test for the Chequing Account.
To run : python -m unittest tests/test_chequing_account.py"""

import unittest
from datetime import date
from bank_account.chequing_account import ChequingAccount

class TestChequingAccount(unittest.TestCase):

    def test_initialize_with_valid_values(self):
        account = ChequingAccount(2004, 2904, 1000.0, date(2024, 10, 3), -100.0, 0.05)
        self.assertEqual(account.account_number, 2004)
        self.assertEqual(account.client_number, 2904)
        self.assertEqual(account.balance, 1000.0)
        self.assertEqual(account._ChequingAccount__overdraft_limit, -100.0)
        self.assertEqual(account._ChequingAccount__overdraft_rate, 0.05)

    def test_initialize_overdraft_limit_value_invalid(self):
        account = ChequingAccount(2004, 2904, 1000.0, date(2024, 10, 3), "invalid", 0.05)
        self.assertEqual(account._ChequingAccount__overdraft_limit, -100.0)

    def test_initialize_overdraft_rate_invalid(self):
        account = ChequingAccount(2004, 2904, 1000.0, date(2024, 10, 3), -100.0, "invalid")
        self.assertEqual(account._ChequingAccount__overdraft_rate, 0.05)

    def test_initialize_account_with_invalid_creation_date(self):
        account = ChequingAccount(2004, 2904, 1000.0, "invalid_date", -100.0, 0.05)
        self.assertEqual(account._date_created, date.today())

    def test_compute_service_charges_when_balance_exceeds_overdraft_limit(self):
        account = ChequingAccount(2004, 2904, 100.0, date(2024, 10, 3), -100.0, 0.05)
        self.assertEqual(account.get_service_charges(), 0.50)

    def test_compute_service_charges_when_balance_below_limit(self):
        account = ChequingAccount(2004, 2904, -600.0, date(2024, 10, 3), -100.0, 0.05)
        self.assertEqual(round(account.get_service_charges(), 2), 25.50)

    def test_compute_service_charges_when_balance_equals_limit(self):
        account = ChequingAccount(2004, 2904, -100.0, date(2024, 10, 3), -100.0, 0.05)
        self.assertEqual(account.get_service_charges(), 0.50)

    def test_account_to_string_method(self):
        account = ChequingAccount(2004, 2904, 1000.0, date(2024, 10, 3), -100.0, 0.05)
        expected_str = ("Account Number: 2004 "
                        "Client Number: 2904 "
                        "Balance: $1,000.00\n"
                        "Overdraft Limit: $-100.00 "
                        "Overdraft Rates: 5.00% "
                        "Account Type: Chequing\n")
        self.assertEqual(str(account), expected_str)

if __name__ == '__main__':
    unittest.main()
