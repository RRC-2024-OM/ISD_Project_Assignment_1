"""
Description: A client program written to verify implementation 
of the Observer Pattern.
Author: ACE Faculty
Edited by: Om Patel
Date: 2024-10-26
"""

# 1.  Import all BankAccount types using the bank_account package
#     Import date
#     Import Client
from bank_account.chequing_account import ChequingAccount
from bank_account.savings_account import SavingsAccount
from datetime import date
from client.client import Client

# 2. Create a Client object with data of your choice.
client_one = Client(client_number = 8888, first_name = "Jayesh", last_name = "Patel", email_address = "jp@gmail.com")

# 3a. Create a ChequingAccount object with data of your choice, using the client_number
chequing_account = ChequingAccount(account_number = 1111, client_number = client_one.client_number, balance = 5896.00, date_created = date.today(), overdraft_limit = -500.00, overdraft_rate = 0.05) 

# 3b. Create a SavingsAccount object with data of your choice, using the client_number 
savings_account = SavingsAccount(account_number = 2222, client_number = client_one.client_number, balance = 14789.00, date_created = date.today(), minimum_balance = 100.00)

# 4 The ChequingAccount and SavingsAccount objects are 'Subject' objects.
# The Client object is an 'Observer' object.  
# 4a.  Attach the Client object (created in step 1) to the ChequingAccount object (created in step 2).
chequing_account.attach(client_one)

# 4a.  Attach the Client object (created in step 1) to the SavingsAccount object (created in step 2).
savings_account.attach(client_one)

# 5a. Create a second Client object with data of your choice.
client_two = Client(client_number = 9999, first_name = "Milan", last_name = "Jot", email_address = "milanjot@gmail.com")

# 5b. Create a SavingsAccount object with data of your choice, using the client_number 
savings_account_two = SavingsAccount(account_number = 7777, client_number = client_two.client_number, balance = 9564.00, date_created = date.today(), minimum_balance = 500.00)

# 6. Use the ChequingAccount and SavingsAccount objects created 
# in steps 3 and 5 above to perform transactions (deposits and withdraws) 
# which would cause the Subject (BankAccount) to notify the Observer 
# (Client) as well as transactions that would not 
# cause the Subject to notify the Observer.  Ensure each 
# BankAccount object performs at least 3 transactions.
# REMINDER: the deposit() and withdraw() methods can raise exceptions
# ensure the methods are invoked using proper exception handling such 
# that any exception messages are printed to the console.

# Transactions for chequing Account
try:
    chequing_account.deposit(11236.01)  
except ValueError as e:
    print(e)

try:
    chequing_account.withdraw(505.00)
except ValueError as e:
    print(e)

try:
    chequing_account.withdraw(6789.00)  
except ValueError as e:
    print(e)

# Transactions for savings_account
try:
    savings_account.deposit(8564.00)
except ValueError as e:
    print(e)

try:
    savings_account.withdraw(13789.00)  
except ValueError as e:
    print(e)

try:
    savings_account.deposit(158.00)
except ValueError as e:
    print(e)

# Transactions for savings_account2
try:
    savings_account_two.deposit(6000.00)
except ValueError as e:
    print(e)

try:
    savings_account_two.withdraw(8500.00)  
except ValueError as e:
    print(e)

try:
    savings_account_two.deposit(500.00)
except ValueError as e:
    print(e)