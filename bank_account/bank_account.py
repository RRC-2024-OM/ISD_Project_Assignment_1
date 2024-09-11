"""Author : Om Patel
Date : 2024-09-11

Description : 
"""

class BankAccount:
    def __init__(self, account_number: int, client_number: int, balance: float):
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

    @property
    def account_number(self) -> int:
        return self.__account_number

    @property
    def client_number(self) -> int:
        return self.__client_number

    @property
    def balance(self) -> float:
        return self.__balance

    def update_balance(self, amount: float):
        try:
            amount = float(amount)
            self.__balance += amount
        except ValueError:
            pass

    def deposit(self, amount: float):
        if not isinstance(amount, (int, float)):
            raise ValueError(f"Deposit amount: {amount} must be numeric.")
        
        if amount <= 0:
            raise ValueError(f"Deposit amount: ${amount:,.2f} must be positive.")
        
        self.update_balance(amount)

    def withdraw(self, amount: float):
        if not isinstance(amount, (int, float)):
            raise ValueError(f"Withdraw amount: {amount} must be numeric.")
        
        if amount <= 0:
            raise ValueError(f"Withdrawal amount: ${amount:,.2f} must be positive.")
        
        if amount > self.__balance:
            raise ValueError(f"Withdrawal amount: ${amount:,.2f} must not exceed the account balance: ${self.__balance:,.2f}")
        
        self.update_balance(-amount)

    def __str__(self) -> str:
        return f"Account: {self.__account_number}, Client: {self.__client_number}, Balance: {self.__balance:.2f}"

