"""
Description : Observer pattern for receiving notifications.
Author : Om Patel 
"""
from abc import ABC, abstractmethod

class Observer(ABC):
    """An abstract base class for observer in the observer design patterns 
        which allows to receive and act to notifications.   

        Methods:
            update (message: str): Abstract method to handle notification updates.
    """
    @abstractmethod
    def update(self, message: str) -> None:
        """Receives a message notification and perform actions.

        Args: 
            message (str): the notification message.

        Raises:
            NotImplementedError: Implemented in subclasses.
        """
        pass