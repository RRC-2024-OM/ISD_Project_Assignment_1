"""
Description: Unit tests for the BankAccount class.
Author: ACE Faculty
Modified by: Om Patel
Date: 2024-09-11
Usage: To execute all tests in the terminal execute 
the following command:
    python -m unittest tests/test_bank_account.py
"""
import unittest
from bank_account.bank_account import BankAccount  

class TestBankAccount(unittest.TestCase):

    def setUp(self):
        self.account = BankAccount(2004, 2904, 10000.00)

    def test_init_attributes(self):
        self.assertEqual(self.account._BankAccount__account_number, 2004)
        self.assertEqual(self.account._BankAccount__client_number, 2904)
        self.assertEqual(round(self.account._BankAccount__balance, 2), 1000.00)

    def test_init_non_numeric_balance(self):
        account = BankAccount(2004, 2904, "not_a_number")
        self.assertEqual(round(account._BankAccount__balance, 2), 0.00)

    def test_init_non_numeric_account_number(self):
        with self.assertRaises(ValueError):
            BankAccount("not_a_number", 2904, 1000.00)

    def test_init_non_numeric_client_number(self):
        with self.assertRaises(ValueError):
            BankAccount(2004, "not_a_number", 1000.00)

    def test_account_number_getter(self):
        self.assertEqual(self.account.account_number, 2004)

    def test_client_number_getter(self):
        self.assertEqual(self.account.client_number, 2904)

    def test_balance_getter(self):
        self.assertEqual(round(self.account.balance, 2), 1000.00)

    def test_update_balance_positive(self):
        self.account.update_balance(500.00)
        self.assertEqual(round(self.account._BankAccount__balance, 2), 1500.00)

    def test_update_balance_negative(self):
        self.account.update_balance(-200.00)
        self.assertEqual(round(self.account._BankAccount__balance, 2), 800.00)

    def test_update_balance_non_numeric(self):
        self.account.update_balance("not_a_number")
        self.assertEqual(round(self.account._BankAccount__balance, 2), 1000.00)

    def test_deposit_valid(self):
        self.account.deposit(150.00)
        self.assertEqual(round(self.account._BankAccount__balance, 2), 1150.00)

    def test_deposit_negative(self):
        with self.assertRaises(ValueError):
            self.account.deposit(-50.00)

    def test_withdraw_valid(self):
        self.account.withdraw(100.00)
        self.assertEqual(round(self.account._BankAccount__balance, 2), 900.00)

    def test_withdraw_negative(self):
        with self.assertRaises(ValueError):
            self.account.withdraw(-50.00)

    def test_withdraw_exceeds_balance(self):
        with self.assertRaises(ValueError):
            self.account.withdraw(2000.00)

    def test_str_method(self):
        self.assertEqual(str(self.account), "Account: 2004, Client: 2904, Balance: 1000.00")

if __name__ == '__main__':
    unittest.main()
