"""Author : Om Patel
Date : 2024-10-03

Description : 
    This module defines a BankAccount class that allows for the creation and manipulation of bank account instances. 
    It supports deposit and withdrawal operations with validation, and provides methods to access account details 
    such as account number, client number, and balance."""

from abc import ABC, abstractmethod
from datetime import date

class BankAccount(ABC):
    """A class used to represent a Bank Account.

    Attributes:
        BASE_SERVICE_CHARGE (float): The base service charge for the bank account.
        account_number (int): The account number for the bank account.
        client_number (int): The client number associated with the bank account.
        balance (float): The initial balance of the bank account.
        date_created (date): The date the account was created."""
    
    BASE_SERVICE_CHARGE: float = 0.50
    
    def __init__(self, account_number: int, client_number: int, balance: float, date_created: date):
        """Initializes a new instance of the BankAccount class.
        
        Args:
            account_number (int): The account number for the bank account.
            client_number (int): The client number associated with the bank account.
            balance (float): The initial balance of the bank account.
            date_created (date): The date account was created.
        
        Raises:
            ValueError: If account_number or client_number are not integers, or if balance cannot be converted to float."""
        
        if not isinstance(account_number, int):
            raise ValueError("Account number must be an integer.")
        self.__account_number = account_number

        if not isinstance(client_number, int):
            raise ValueError("Client number must be an integer.")
        self.__client_number = client_number

        try:
            self.__balance = float(balance)
        except ValueError:
            self.__balance = 0.0

        if isinstance(date_created, date):
            self._date_created = date_created
        else:
            self._date_created = date.today()

    @property
    def account_number(self) -> int:
        """Gets the account number of the bank account.
        
        Returns:
            int: The account number of the bank account."""
        return self.__account_number

    @property
    def client_number(self) -> int:
        """Gets the client number associated with the bank account.
        
        Returns:
            int: The client number associated with the bank account."""
        return self.__client_number

    @property
    def balance(self) -> float:
        """Gets the current balance of the bank account.
        
        Returns:
            float: The current balance of the bank account."""
        return self.__balance

    def update_balance(self, amount: float):
        """Updates the balance of the bank account by the given amount.
        
        Args:
            amount (float): The amount to be added to the current balance.
        
        Note:
            The amount is expected to be a float. If it cannot be converted to float, no update occurs."""
        
        try:
            amount = float(amount)
            self.__balance += amount
        except ValueError:
            raise ValueError("Amount must be a numeric value.")
        

    def deposit(self, amount: float):
        """Deposits the given amount into the bank account.
        
        Args:
            amount (float): The amount to deposit into the bank account.
        
        Raises:
            ValueError: If the amount is not numeric or is less than or equal to zero."""
        
        if not isinstance(amount, (int, float)):
            raise ValueError(f"Deposit amount: {amount} must be numeric.")
        
        if amount <= 0:
            raise ValueError(f"Deposit amount: ${amount:,.2f} must be positive.")
        
        self.update_balance(amount)

    def withdraw(self, amount: float):
        """Withdraws the given amount from the bank account.
        
        Args:
            amount (float): The amount to withdraw from the bank account.
        
        Raises:
            ValueError: If the amount is not numeric, is less than or equal to zero, or exceeds the current balance."""
        
        if not isinstance(amount, (int, float)):
            raise ValueError(f"Withdraw amount: {amount} must be numeric.")
        
        if amount <= 0:
            raise ValueError(f"Withdrawal amount: ${amount:,.2f} must be positive.")
        
        if amount > self.__balance:
            raise ValueError(f"Withdrawal amount: ${amount:,.2f} must not exceed the account balance: ${self.__balance:,.2f}")
        
        self.update_balance(-amount)

    def __str__(self) -> str:
        """Provides a string representation of the bank account.
        
        Returns:
            str: A string representation of the account number, client number, and current balance."""
        
        return (f"Account: {self.__account_number}"
                f"Client: {self.__client_number}"
                f"Balance: {self.__balance:.2f}\n")
    
    @abstractmethod
    def get_service_charges(self) -> float:
        """Abstract method to return the calculated service charges.
        Returns:
            float: The calculated service charges for the bank account."""
        pass
