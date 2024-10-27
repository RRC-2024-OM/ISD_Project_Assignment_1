"""
Description: Service charge strategy is for calculating service charges.
Author: Om Patel
"""
from abc import ABC, abstractmethod

class ServiceChargeStrategy(ABC):
    """A foundational abstract class that outlines a method for determining 
    service charges on bank accounts.

    Attribute:
        BASE_SERVICE_CHARGE (float): The standard base service charge that is 
        applied to accounts.

    Methods:
        calculate_service_charges(account) -> float: An abstract method for 
        determining service charges, intended to be implemented by subclasses.
    """
    BASE_SERVICE_CHARGE = 0.50

    @abstractmethod
    def calculate_service_charges(self, account) -> float:
        """Determines the service charges for the specified bank account.

        Args:
            account: The specific bank account instance that requires service 
            charge calculation.

        Returns: 
            float: The service charge that has been determined for the account.
        """
        pass 