"""Author:Om Patel

Description : the Client class to represent client details including client number, 
first name, last name, and email address. The class validates input data, 
ensuring non-blank names and a valid email address.
"""
from email_validator import validate_email, EmailNotValidError
from patterns.observer.observer import Observer
from utility.file_utils import simulate_send_email
from datetime import datetime

class Client(Observer):
    """
    Represents a client with personal details.
    """
    def __init__(self, client_number: int, first_name: str, last_name: str, email_address: str):
        """
        Initializes a new Client instance.

        Args:
            client_number (int): The client's unique number.
            first_name (str): The client's first name.
            last_name (str): The client's last name.
            email_address (str): The client's email address.
    
        Raises:
            ValueError: Raised when client_number is not an integer.
            ValueError: Raised when first_name is blank after stripping whitespace.
            ValueError: Raised when last_name is blank after stripping whitespace.

        """
        if not isinstance(client_number, int):
            raise ValueError("Client number should be numeric.")
    
        if len(first_name.strip()) == 0:
            raise ValueError("First name cannot be blank.")

        if len(last_name.strip()) == 0:
            raise ValueError("Last name cannot be blank.")

        self.__client_number = client_number
        self.__first_name = first_name
        self.__last_name = last_name

        try:
            valid = validate_email(email_address)
            self.__email_address = valid.email
        except EmailNotValidError:
            self.__email_address = "om.patel@pixell-river.com"

    @property
    def client_number(self) -> int:
        """
        Gets the client's number.
    
        Returns:
            int: The client's unique number.
        """
        return self.__client_number

    @property
    def first_name(self) -> str:
        """
        Gets the client's first name.
    
        Returns:
            str: The client's first name.
        """
        return self.__first_name

    @property
    def last_name(self) -> str:
        """
        Gets the client's last name.

        Returns:
            str: The client's last name.
        """
        return self.__last_name

    @property
    def email_address(self) -> str:
        """
        Gets the client's email address.

        Returns:
            str: The client's email address.
        """
        return self.__email_address

    def __str__(self) -> str:
        """
        Returns the "informal" or nicely printable string representation of the Client instance.

        Returns:
            str: The "informal" or nicely printable string representation of the client's last name, first name,
            client number, and email address.
        """
        return (
            f"Name: {self.__last_name}, {self.__first_name}\n"
            f"Client Number: {self.__client_number}\n"
            f"Email Address: {self.__email_address}\n"
        )
    
    def update(self, message: str) -> None:
        """Send an update message notification to the client in case any new activity is being there
        in account by simulating an email.

        Args:
            message (str) : The message regrading new activity with took place in account.
        """
        subject = f"ALERT: Unusual Activity: {datetime.now()}"

        notification_message = (f"Notification for {self.__client_number}: " 
                                f"{self.__first_name} {self.__last_name}: {message}")
        
        simulate_send_email(self.__email_address, subject, notification_message)
