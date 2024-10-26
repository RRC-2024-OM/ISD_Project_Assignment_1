"""Author: Om Patel
Date: 2024-10-25

Description : This module defines a SavingsAccount class that is sub class of BankAccount class.
It has attributes and required methods for the Saving Account.
"""

from datetime import date
from bank_account.bank_account import BankAccount
from patterns.strategy.minimum_balance_strategy import MinimumBalanceStrategy

class SavingsAccount(BankAccount):
    """The class represent Savings Account inherits for BankAccount which is superclass abstract.

    Attributes:
        SERVICE_CHARGE_PREMIUM (float): Savings Account premium service charges.

        minimum_balance (float): Savings account minimum balance.
    """
    def __init__(self, account_number: int, client_number: int, balance: float, date_created: date, minimum_balance: float):
        """New SavingsAccount class created.

        Arguments:
            account_number (int): The account number for the bank account.
            client_number (int): The client number associated with the bank account.
            balance (float): The initial balance of the bank account.
            date_created (date): The date account was created.
            minimum_balance (float): Savings account 
        """
        super().__init__(account_number, client_number, balance, date_created)

        try:
            self.__minimum_balance = float(minimum_balance)
        except ValueError:
            self.__minimum_balance = 50.0

        #MinimumBalanceStrategy
        self._service_charge_strategy = MinimumBalanceStrategy(self.__minimum_balance)

    def __str__(self) -> str:
        """String for Savings Account.

        Returns:
            Str: A string representing account_number, client_number, balance, date_created, and minimum_balance.
        """

        return (f"Account Number: {self.account_number} "
                f"Client Number: {self.client_number} "
                f"Balance: ${self.balance:,.2f}\n"
                f"Minimum Balance: ${self.__minimum_balance:,.2f} "
                f"Account Type: Savings\n")
    
    def get_service_charges(self) -> float:
        """Returns the calculated service charge.

        Returns:
            float: The service charge calculation for savings account.
        """

        return self._service_charge_strategy.calculate_service_charges(self)
