# Intermediate Software Development Automated Teller Project

This project will be developed over the course of several assignments. Each  
assignment will build on the work done in the previous assignment(s). Ultimately,  
an entire system will be created to manage bank transactions for clients who  
have one or more bank accounts.

## Author

Om Patel

### Assignment

#### Assignment 1 :  Automated Teller Project*

In this assignment i developed of two core classes: BankAccount and Client. The BankAccount class manages bank account details and transactions, while the Client class handles client information. The goal is to implement encapsulation to protect internal data and provide controlled access through methods and properties.

##### Encapsulation

##### Bank Account Class

In the BankAccount class, private attributes such as __account_number,__client_number, and __balance are hidden from direct access to prevent unauthorized changes. Public properties and methods, like deposit, withdraw, and update_balance, allow controlled interactions, ensuring that the balance is modified only under valid conditions.

###### Assignment 2: Abstraction, Inheritance and Polymorphism

###### How Polymorphism Was Achieved

1. **Inheritance**: Each subclass (ChequingAccount, SavingsAccount, and InvestmentAccount) inherits from the base class BankAccount. This means that each subclass inherits the attributes and methods of the BankAccount class.

2. **Method Overriding**: The subclasses override the 'get_service_charges' method from the BankAccount class to provide specific implementations based on the account type. This allows each subclass to calculate service charges differently while maintaining a common interface.

3. **Polymorphic Behavior**: By using the common interface provided by the BankAccount class, we can treat instances of the subclasses as instances of the BankAccount class. This allows us to write code that works with any type of bank account without knowing the specific subclass.

###### Assignment 3: Design Patterns 