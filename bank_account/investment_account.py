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
    