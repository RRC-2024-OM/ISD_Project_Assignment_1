"""
Description: Pattern implementation for calculating overdraft fees.
Author: Om Patel 
"""
from patterns.strategy.service_charge_strategy import ServiceChargeStrategy
from bank_account.bank_account import BankAccount

class OverdraftStrategy(ServiceChargeStrategy):
    """A strategy for calculating service charges based on an overdraft limit. If the account balance is 
    below the overdraft limit, an additional fee is calculated based on the overdraft rate.

    Attributes:
        _overdraft_limit (float): The balance that must be maintained to prevent overdraft fees.
        _overdraft_rate (float): The interest rate applied to calculate fees for overdrafts below the limit.

    Methods:
        calculate_service_charges(account: BankAccount) -> float: Imposes service charges when the account balance 
        is less than the overdraft limit.
    """
    def __init__(self, overdraft_limit: float, overdraft_rate: float):
        """
        """
        self.__overdraft_limit = overdraft_limit
        self.__overdraft_rate = overdraft_rate

    def calculate_service_charges(self, account: BankAccount) -> float:
        """Computes the service charge for the account, adding an overdraft fee to the base charge if the balance is below the limit.

        Args:
            account (BankAccount): The bank account that needs service charges calculated.

        Returns:
            float: The overall service charge, factoring in any overdraft fees that may apply.
        """
        if account.balance >= self.__overdraft_limit:
            return self.BASE_SERVICE_CHARGE
        else:
            overdraft_interest = (self.__overdraft_limit - account.balance) * self.__overdraft_rate
            return self.BASE_SERVICE_CHARGE + overdraft_interest