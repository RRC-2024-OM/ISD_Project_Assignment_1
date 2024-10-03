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

    def __str__(self) -> str:
        """String for Investment account.

        Returns:
            A string representing account_number, client_number, balance, date_created and management fee."""
        
        if self._date_created > self.TEN_YEARS_AGO:
            management_fee_str = f"${self.__management_fee:,.2f}"
        else:
            management_fee_str = "Waived"

        return (f"Account Number: {self.account_number} "
                f"Client Number: {self.client_number} "
                f"Balance: ${self.balance:,.2f}\n"
                f"Date Created: {self._date_created} "
                f"Management Fee: {management_fee_str} "
                f"Account Type: Investment\n")
    
    def get_service_charges(self) -> float:
        """Returns the calculated service charge for the investment account.

        Returns:
            float: The service charge for the investment account."""
        if self._date_created > self.TEN_YEARS_AGO:
            return self.BASE_SERVICE_CHARGE + self.__management_fee
        else:
            return self.BASE_SERVICE_CHARGE
