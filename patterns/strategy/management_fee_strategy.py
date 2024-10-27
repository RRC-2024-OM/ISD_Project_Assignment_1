"""
Description : Strategy for calculating management fees.
Author : Om Patel
"""
from datetime import date, timedelta
from bank_account.bank_account import BankAccount
from patterns.strategy.service_charge_strategy import ServiceChargeStrategy

class ManagementFeeStrategy(ServiceChargeStrategy):
    """A strategy for calculating service charges based on account creation date 
    and an additional management fee if the account is less than ten years old.

        Attributes:
            TEN_YEARS_AGO (date): A constant representing the date exactly ten years ago.

        Method:
            calculate_service_charges(account: BankAccount) -> float: Calculates fees for services 
            based on the date the account was opened.
    """
    TEN_YEARS_AGO = date.today() - timedelta(days = 10 * 365.25)

    def __init__(self, date_created: date, management_fee: float):
        """Configures the ManagementFeeStrategy by incorporating the account creation date and the 
        management fee.

        Args:
            date_created (date): Acount creation date.
            management_fee (float): The extra management fee is charged to newer accounts.
        """
        self.__date_created = date_created
        self.__management_fee = management_fee

    def calculate_service_charges(self, account: BankAccount) -> float:
        """Evaluates the total service charge for the account, with an added management fee for 
        accounts created in the past ten years.

        Args:
            account (BankAcount): The bank account for which to calculate service charges.

        Returns:
            float: The total cost of services, incorporating any management fees that apply.
        """
        if self.__date_created > self.TEN_YEARS_AGO:
            return self.BASE_SERVICE_CHARGE + self.__management_fee
        else:
            return self.BASE_SERVICE_CHARGE
        