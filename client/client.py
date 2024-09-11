"""Description: This module defines a Client class that manages client details like client number,
 name, and email, with validation for each field. Invalid emails default to a placeholder. It
 includes methods to access client information and a formatted string representation.
Author: Om patel
"""

from email_validator import validate_email, EmailNotValidError

class Client:
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
            self.__email_address = "email@pixell-river.com"
 
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
        """Returns the "informal" or nicely printable string representation of the Client instance.
 
        Returns:
            The "informal" or nicely printable string representation of the client's last name, first name,
            client number, and email address.
        """
        return (
            f"Name: {self.__last_name}, {self.__first_name}\n"
            f"Client Number: {self.__client_number}\n"
            f"Email Address: {self.__email_address}\n"
        )


