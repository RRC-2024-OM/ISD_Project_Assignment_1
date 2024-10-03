"""Author : Om Patel
Date : 2024-10-03

Description : This module defines a ChequingAccount class that is sub class of BankAccount class.
It has attributes and required methods for the Chequing Account."""

from datetime import date
from bank_account.bank_account import BankAccount

class ChequingAccount(BankAccount):
    """Class representing Chequing Account, which inherits from the BackAccount class.

    Attributes:
        overdraft_limit (float): The maximum amount a balance can be overdrawn before 
        incurring overdraft fees.
        overdraft_rate (float): Rate for the incurring overdraft fees which will be applicable."""
    
    def __init__(self, account_number: int, client_number: int, balance: float, date_created: date, overdraft_limit: float, overdraft_rate: float):
        """New ChequingAccount class created.

        Arguments:
            account_number (int): The account number for the bank account.
            client_number (int): The client number associated with the bank account.
            balance (float): The initial balance of the bank account.
            date_created (date): The date the account was created."""
        
        super().__init__(account_number, client_number, balance, date_created)

        try:
            self.__overdraft_limit = float(overdraft_limit)
        except ValueError:
            self.__overdraft_limit = -100.0

        try:
            self.__overdraft_rate = float(overdraft_rate)
        except ValueError:
            self.__overdraft_rate = 0.05


