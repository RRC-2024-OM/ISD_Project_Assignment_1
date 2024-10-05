"""
Description: A client program written to verify correctness of 
the BankAccount sub classes.
Author: ACE Faculty
Edited by: Om Patel
Date: 2024-10-05
"""

# 1.  Import all BankAccount types using the bank_account package
#     Import date from datetime
from bank_account import *
from datetime import date

# 2. Create an instance of a ChequingAccount with values of your 
# choice including a balance which is below the overdraft limit.
try:
    chequing_account = ChequingAccount(2004, 2904, -150.0, date.today(), -100.0, 0.05)
except Exception as e:
    print(f"Error creating ChequingAccount: {e}")

# 3. Print the ChequingAccount created in step 2.
try:
    print(chequing_account)
except Exception as e:
    print(f"Error printing ChequingAccount: {e}")

# 3b. Print the service charges amount if calculated based on the 
# current state of the ChequingAccount created in step 2.
try:
    print(f"Service Charges: {chequing_account.get_service_charges()}")
except Exception as e:
    print(f"Error calculating service Charges: {e}")

# 4a. Use ChequingAccount instance created in step 2 to deposit 
# enough money into the chequing account to avoid overdraft fees.
try:
    chequing_account.deposit(800.0)
except Exception as e:
    print (f"Error depositing money: {e}")

# 4b. Print the ChequingAccount
try:
    print(chequing_account)
except Exception as e:
    print(f"Error printing ChequingAccount: {e}")

# 4c. Print the service charges amount if calculated based on the 
# current state of the ChequingAccount created in step 2.
try:
    print(f"Service Charges: {chequing_account.get_service_charges()}")
except Exception as e:
    print(f"Error calculating service charges: {e}")

print("===================================================")
# 5. Create an instance of a SavingsAccount with values of your 
# choice including a balance which is above the minimum balance.
try:
    savings_account = SavingsAccount(2004, 2904, 1000.00, date.today(), 50.0)
except Exception as e:
    print(f"Error creating SavingsAccount: {e}")

# 6. Print the SavingsAccount created in step 5.
try:
    print(savings_account)
except Exception as e:
    print(f"Error printing SavingsAccount: {e}")

# 6b. Print the service charges amount if calculated based on the 
# current state of the SavingsAccount created in step 5.
try:
    print(f"Service Charges: {savings_account.get_service_charges()}")
except Exception as e:
    print(f"Error calculating service charges: {e}")

# 7a. Use this SavingsAccount instance created in step 5 to withdraw 
# enough money from the savings account to cause the balance to fall 
# below the minimum balance.

# 7b. Print the SavingsAccount.
# 7c. Print the service charges amount if calculated based on the 
# current state of the SavingsAccount created in step 5.



print("===================================================")
# 8. Create an instance of an InvestmentAccount with values of your 
# choice including a date created within the last 10 years.


# 9a. Print the InvestmentAccount created in step 8.
# 9b. Print the service charges amount if calculated based on the 
# current state of the InvestmentAccount created in step 8.


# 10. Create an instance of an InvestmentAccount with values of your 
# choice including a date created prior to 10 years ago.


# 11a. Print the InvestmentAccount created in step 10.
# 11b. Print the service charges amount if calculated based on the 
# current state of the InvestmentAccount created in step 10.


print("===================================================")

# 12. Update the balance of each account created in steps 2, 5, 8 and 10 
# by using the withdraw method of the superclass and withdrawing 
# the service charges determined by each instance invoking the 
# polymorphic get_service_charges method.



# 13. Print each of the bank account objects created in steps 2, 5, 8 and 10.

