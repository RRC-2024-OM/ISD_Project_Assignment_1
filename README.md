# Intermediate Software Development Automated Teller Project

This project will be developed over the course of several assignments. Each  
assignment will build on the work done in the previous assignment(s). Ultimately,  
an entire system will be created to manage bank transactions for clients who  
have one or more bank accounts.

## Author

Om Patel

## Assignment

### Assignment 1 :  Automated Teller Project*

In this assignment i developed of two core classes: BankAccount and Client. The BankAccount class manages bank account details and transactions, while the Client class handles client information. The goal is to implement encapsulation to protect internal data and provide controlled access through methods and properties.

#### Encapsulation

#### Bank Account Class

In the BankAccount class, private attributes such as __account_number,__client_number, and __balance are hidden from direct access to prevent unauthorized changes. Public properties and methods, like deposit, withdraw, and update_balance, allow controlled interactions, ensuring that the balance is modified only under valid conditions.

### Assignment 2: Abstraction, Inheritance and Polymorphism

#### How Polymorphism Was Achieved

1. **Inheritance**: Each subclass (ChequingAccount, SavingsAccount, and InvestmentAccount) inherits from the base class BankAccount. This means that each subclass inherits the attributes and methods of the BankAccount class.

2. **Method Overriding**: The subclasses override the 'get_service_charges' method from the BankAccount class to provide specific implementations based on the account type. This allows each subclass to calculate service charges differently while maintaining a common interface.

3. **Polymorphic Behavior**: By using the common interface provided by the BankAccount class, we can treat instances of the subclasses as instances of the BankAccount class. This allows us to write code that works with any type of bank account without knowing the specific subclass.

### Assignment 3: Design Patterns

#### Strategy Patterns

The bank charges are calculated depending on the kind of account using the Strategy Pattern. Through this method, calculation logic is divorced from the BankAccount classes. This reduces the system development overhead by isolating the calculation logic.

##### Implementation

1. **ServiceChargeStrategy** : An abstract class that defines one common place where all service charge calculation strategies.
2. **ManagementFeeStrategy** : Strategy for calculating service charge for InvestmentAccount.
3. **OverdraftStrategy** : Strategy for calculating service for ChequingAccount.
4. **MinimumBalanceStrategy** : Strategy for calculating service for SavingsAccount.

Each BankAccount subclass contains a private strategy instance. The get_service_charge method calls this instance to compute service charges, 
keeping the logic modular and easily adjustable.

#### Observer Patterns

The observer patterns is used to notify the user about account activities.

1. **Observer** : An abstract class that defines one common place where all notification.
2. **Subject** : A class that maintains the list of observers and there notifications.
3. **Client** : Implements the observer.
4. **BankAccount** : Implements the subject and notifies its observes of any activity.

With the use of observer patterns, the application ensure that client will get notifications of important activities.

### Assignment 4 Event-Driven Programming Paradigm

This application employs the Event-Driven Programming Paradigm to handle user interactions and system responses dynamically. In an event-driven architecture, the flow of the program is determined by events such as user actions (clicks, key presses), sensor outputs, or messages from other programs.

#### Key Components

1. **Signals and Slots**:
    - Signals: In this application, signals are emitted to indicate that an event has occurred. For example, when a transaction is applied (deposit or withdraw) in the AccountDetailsWindow, a signal is emitted to notify the ClientLookupWindow.
    - Slots: Slots are functions that are called in response to a particular signal. In this application, the ClientLookupWindow has a slot (update_data) that updates the account balance in the table when it receives a signal from the AccountDetailsWindow.

2. **Event Handlers**:
    - *Button Clicks*: The application connects button clicks (e.g., deposit, withdraw, exit) to specific event handlers. These handlers perform actions such as applying a transaction or closing a window.
    - *Table Cell Clicks*: Clicking on a table cell in the ClientLookupWindow triggers an event handler that opens the AccountDetailsWindow for the selected account.

3. **Dynamic Updates**:
    - The use of signals and slots allows the application to update the user interface dynamically. When the balance of an account is updated in the AccountDetailsWindow, the change is immediately reflected in the ClientLookupWindow without the need for manual refreshing.
