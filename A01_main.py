"""
Description: A client program written to verify correctness of 
the BankAccount and Client classes.
Author: ACE Faculty
Edited by: Om Patel
Date: 2024-09-11
"""

from bank_account.bank_account import BankAccount
from client.client import Client

def main():
    # 1. Code a statement which creates a valid instance of the Client class.
    # Use your own unique valid values for the inputs to the class.
    try:
        client = Client(client_number=2904, first_name="Om", last_name="Patel", email_address="om.patel@example.com")
    except ValueError as e:
        print(f"Error creating Client: {e}")

    # 2. Declare a BankAccount object with an initial value of None.
    bank_account = None

    # 3. Using the bank_account object declared in step 2, code a statement
    # to instantiate the BankAccount object.
    # Use any integer value for the BankAccount number.
    # Use the client_number used to create the Client object in step 1 for the
    # BankAccount's client_number.
    # Use a floating point value for the balance.
    try:
        bank_account = BankAccount(account_number= 2004, client_number=client.client_number, balance=1000.0)
    except ValueError as e:
        print(f"Error creating BankAccount: {e}")

    # 4. Code a statement which creates an instance of the BankAccount class.
    # Use any integer value for the BankAccount number.
    # Use the client_number used to create the Client object in step 1 for the
    # BankAccount's client_number.
    # Use an INVALID value (non-float) for the balance.
    try:
        invalid_bank_account = BankAccount(account_number=67890, client_number=client.client_number, balance="invalid_balance")
    except ValueError as e:
        print(f"Error creating BankAccount with invalid balance: {e}")

    # 5. Code a statement which prints the Client instance created in step 1.
    # Code a statement which prints the BankAccount instance created in step 3.
    print("Client Information:")
    print(client)
    
    print("BankAccount Information:")
    print(bank_account)

    # 6. Attempt to deposit a non-numeric value into the BankAccount created in step 3.
    try:
        bank_account.deposit("non_numeric_value")
    except ValueError as e:
        print(f"Deposit Error: {e}")

    # 7. Attempt to deposit a negative value into the BankAccount created in step 3.
    try:
        bank_account.deposit(-100.0)
    except ValueError as e:
        print(f"Deposit Error: {e}")

    # 8. Attempt to withdraw a valid amount of your choice from the BankAccount created in step 3.
    try:
        bank_account.withdraw(100.0)
    except ValueError as e:
        print(f"Withdrawal Error: {e}")

    # 9. Attempt to withdraw a non-numeric value from the BankAccount created in step 3.
    try:
        bank_account.withdraw("non_numeric_value")
    except ValueError as e:
        print(f"Withdrawal Error: {e}")

    # 10. Attempt to withdraw a negative value from the BankAccount created in step 3.
    try:
        bank_account.withdraw(-50.0)
    except ValueError as e:
        print(f"Withdrawal Error: {e}")

    # 11. Attempt to withdraw a value from the BankAccount created in step 3 which
    # exceeds the current balance of the account.
    try:
        bank_account.withdraw(10000.0)
    except ValueError as e:
        print(f"Withdrawal Error: {e}")

    # 12. Code a statement which prints the BankAccount instance created in step 3.
    print("Updated BankAccount Information:")
    print(bank_account)

if __name__ == "__main__":
    main()