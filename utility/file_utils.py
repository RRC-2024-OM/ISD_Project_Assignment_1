"""Utility functions for file operations."""

import os

@staticmethod
def simulate_send_email(email_address: str, subject: str, message: str) -> None:
    """
    Sends a 'simulated' email by writing the email content to a file.

    The message will appear in the 'observer_emails.txt' file within 
    the 'output' directory of the current project directory.

    Args:
        email_address (str): The recipient's email address.
        subject (str): The subject line for the email.
        message (str): The email message body.
    """
    directory = "output"
    filename = "observer_emails.txt"
    path = os.path.join(directory, filename)
    os.makedirs(directory, exist_ok=True)
    with open(path, "a") as file:
        file.write(f"---\nTo: {email_address}\nSubject: {subject}\nMessage: {message}\n---\n")
