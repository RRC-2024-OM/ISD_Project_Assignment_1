"""
Description: This module defines the ClientLookupWindow class for handling client lookup and account selection in the banking application.
Author: Om Patel
"""

from PySide6.QtWidgets import QTableWidgetItem, QMessageBox
from PySide6.QtCore import Qt, Slot
from ui_superclasses.lookup_window import LookupWindow
from user_interface.account_details_window import AccountDetailsWindow
from user_interface.manage_data import load_data, update_data
from bank_account.bank_account import BankAccount

class ClientLookupWindow(LookupWindow):
    """
    A class used to handle client lookup and account selection in the banking application.
    """

    def __init__(self) -> None:
        """
        Initializes the ClientLookupWindow by setting up connections and loading data.
        
        Returns:
            None
        """
        super().__init__()
        self.__client_listing, self.__accounts = load_data()
        self.lookup_button.clicked.connect(self.__on_lookup_client)
        self.account_table.cellClicked.connect(self.__on_select_account)

    def __on_lookup_client(self) -> None:
        """
        Handles the client lookup event by displaying client details and associated bank accounts.
        
        Returns:
            None
        """
        try:
            client_number = int(self.client_number_edit.text())
        except ValueError:
            QMessageBox.critical(self, "Non-Numeric Client", "Client number must be numeric.")
            self.reset_display()
            return

        if client_number not in self.__client_listing:
            QMessageBox.critical(self, "Client Not Found", f"Client number {client_number} does not exist.")
            self.reset_display()
            return

        client = self.__client_listing[client_number]
        self.client_info_label.setText(f"{client.last_name}, {client.first_name} [{client.client_number}] - {client.email_address}")

        self.account_table.setRowCount(0)
        for account in self.__accounts.values():
            if account.client_number == client_number:
                row_position = self.account_table.rowCount()
                self.account_table.insertRow(row_position)

                self.account_table.setItem(row_position, 0, QTableWidgetItem(str(account.account_number)))
                self.account_table.setItem(row_position, 1, QTableWidgetItem(f"${account.balance:,.2f}"))
                self.account_table.setItem(row_position, 2, QTableWidgetItem(str(account._date_created)))
                self.account_table.setItem(row_position, 3, QTableWidgetItem(account.__class__.__name__))

        self.account_table.resizeColumnsToContents()

    @Slot(int, int)
    def __on_select_account(self, row: int, column: int) -> None:
        """
        Handles the account selection event by opening the Account Details window.
        
        Args:
            row (int): The row index of the selected cell.
            column (int): The column index of the selected cell.
        
        Returns:
            None
        """
        account_number_item = self.account_table.item(row, 0)
        if account_number_item is None:
            QMessageBox.critical(self, "Invalid Selection", "No account selected.")
            return

        account_number = int(account_number_item.text())
        if account_number not in self.__accounts:
            QMessageBox.critical(self, "Bank Account Does Not Exist", "Selected bank account does not exist.")
            return

        account = self.__accounts[account_number]
        account_details_window = AccountDetailsWindow(account)

        account_details_window.balance_updated.connect(self.update_data)

        account_details_window.exec_()

    @Slot(BankAccount)
    def update_data(self, account: BankAccount) -> None:
        """
        Updates the account balance in the table and in the accounts dictionary.
        
        Args:
            account (BankAccount): The bank account with the updated balance.
        
        Returns:
            None
        """
        for row in range(self.account_table.rowCount()):
            account_number_item = self.account_table.item(row, 0)
            if account_number_item and int(account_number_item.text()) == account.account_number:
                self.account_table.setItem(row, 1, QTableWidgetItem(f"${account.balance:,.2f}"))

        # Update the accounts dictionary
        self.__accounts[account.account_number] = account

        # Update the accounts.csv file
        update_data(account)

