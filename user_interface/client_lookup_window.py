"""
Description: This module defines the ClientLookupWindow class for handling client lookup and account selection in the banking application.
Author: Om Patel
"""

from PySide6.QtWidgets import QTableWidgetItem, QMessageBox
from PySide6.QtCore import Qt

from ui_superclasses.lookup_window import LookupWindow
from user_interface.account_details_window import AccountDetailsWindow
from user_interface.manage_data import load_data
from user_interface.manage_data import update_data
from bank_account.bank_account import BankAccount

class ClientLookupWindow(LookupWindow):

    def __init__(self):
        
        super().__init__()
        self.__client_listing, self.__accounts = load_data()
        self.lookup_button.clicked.connect(self.__on_lookup_client)  
        self.account_table.cellClicked.connect(self.__on_select_account)  
    
    def __on_lookup_client(self):
        
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
                self.account_table.setItem(row_position, 2, QTableWidgetItem(str(account._date_created)))  # Updated to use _date_created
                self.account_table.setItem(row_position, 3, QTableWidgetItem(account.__class__.__name__))

        self.account_table.resizeColumnsToContents()
        
