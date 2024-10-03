"""Author : Om Patel
Date : 2024-10-3

Description :  This module defines a InvestmentAccount class that is sub class of BankAccount class.
It has attributes and required methods for the Investment Account.
"""
from datetime import date, timedelta
from bank_account.bank_account import BankAccount

class InvestmentAccount(BankAccount):
    """The class represent Investment Account inherits for BankAccount which is superclass abstract.

    Attributes:
        TEN_YEARS_AGO (date): Gets the date ten years ago from present today.
        management_fee (float) : Fees for managing the investment account."""
    
    TEN_YEARS_AGO = date.today() - timedelta(days=10 * 365.25)

    def __init__(self, account_number: int, client_number: int, balance: float, date_created: date, management_fee: float):
        """New InvestmentAccount class created.

        Arguments:
            account_number (int): The account number for the bank account.
            client_number (int): The client number associated with the bank account.
            balance (float): The initial balance of the bank account.
            date_created (date): The date account was created.
            management_fee (float): The fee for the investment account management."""
        
        super().__init__(account_number, client_number, balance, date_created)

        try:
            self.__management_fee = float(management_fee)
        except ValueError:
            self.__management_fee = 2.55

