"""
Description: This module defines the AccountDetailsWindow class for handling account details and transactions in the banking application.
Author: Om Patel
"""

from PySide6.QtWidgets import QDialog, QMessageBox
from PySide6.QtCore import Signal, Slot
from ui_superclasses.details_window import DetailsWindow
from bank_account.bank_account import BankAccount
import copy

class AccountDetailsWindow(DetailsWindow):
    balance_updated = Signal(BankAccount)  

    def __init__(self, account: BankAccount) -> None:

        super().__init__()
        if isinstance(account, BankAccount):
            self.account = copy.copy(account)
            self.account_number_label.setText(str(self.account.account_number))
            self.balance_label.setText(f"${self.account.balance:,.2f}")

            self.deposit_button.clicked.connect(self.__on_apply_transaction)
            self.withdraw_button.clicked.connect(self.__on_apply_transaction)
            self.exit_button.clicked.connect(self.__on_exit)
        else:
            self.reject()

    def __on_apply_transaction(self):
        try:
            amount = float(self.transaction_amount_edit.text())
        except ValueError:
            QMessageBox.critical(self, "Transaction Failed", "Invalid amount. Please enter a numeric value.")
            self.transaction_amount_edit.setFocus()
            return

        try:
            transaction_type = None
            if self.sender() == self.deposit_button:
                transaction_type = "Deposit"
                self.account.deposit(amount)
            elif self.sender() == self.withdraw_button:
                transaction_type = "Withdraw"
                self.account.withdraw(amount)

            self.balance_label.setText(f"${self.account.balance:,.2f}")
            self.transaction_amount_edit.setText("")
            self.transaction_amount_edit.setFocus()

            #Signal Emission
            self.balance_updated.emit(self.account)
        except Exception as e:
            QMessageBox.critical(self, "Transaction Failed", f"{transaction_type} failed: {e}")
            self.transaction_amount_edit.setText("")
            self.transaction_amount_edit.setFocus()

    def __on_exit(self):
        self.close()

