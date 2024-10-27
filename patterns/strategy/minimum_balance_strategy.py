"""
Description : Strategy for service charge calculation.
Author: Om Patel
"""
from patterns.strategy.service_charge_strategy import ServiceChargeStrategy
from bank_account.bank_account import BankAccount

class MinimumBalanceStrategy(ServiceChargeStrategy):
    """A framework for calculating service fees depending on whether an account 
    maintains the required minimum balance. Accounts that fall short of this balance 
    incur an extra premium charge.

    Attributes:
        SERVICE_CHARGE_PREMIUM (float):The rate applied to the base service fee when the 
        balance does not meet the minimum requirement. 

    Methods:
        Determines service charges by comparing the accounts balance to the minimum required balance.
    """
    SERVICE_CHARGE_PREMIUM: float = 2.00

    def __init__(self, minimum_balance: float):
        """Initializes the MinimumBalanceStrategy with a specified minimum balance requirement.

        Args:
            minimum_balance (float): The minimum amount required in the account to prevent the premium 
            service fee.
        """
        self.__minimum_balance = minimum_balance

    def calculate_service_charges(self, account: BankAccount) -> float:
        """Determines the service charge for the account, adding a premium fee if the account balance 
        is under the minimum required.

        Args:
            account (BankAccount): The account for which the bank must calculate service charges.

        Returns:
            float: The total service charge calculated, factoring in a premium if the balance is below 
            the specified minimum.
        """
        if account.balance >= self.__minimum_balance:
            return self.BASE_SERVICE_CHARGE
        else:
            return self.BASE_SERVICE_CHARGE * self.SERVICE_CHARGE_PREMIUM
