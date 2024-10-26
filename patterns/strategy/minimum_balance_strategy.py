"""
Description : Strategy for service charge calculation.
Author: Om Patel
"""
from strategy.service_charge_strategy import ServiceChargeStrategy
from bank_account.bank_account import BankAccount

class MinimumBalanceStrategy(ServiceChargeStrategy):
    SERVICE_CHARGE_PREMIUM: float = 2.00

    def __init__(self, minimum_balance: float):
        self.__minimum_balance = minimum_balance

    
