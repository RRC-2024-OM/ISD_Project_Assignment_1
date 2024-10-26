"""
Description : Observer pattern for receiving notifications.
Author : Om Patel 
"""
from abc import ABC, abstractmethod

class Observer(ABC):
    @abstractmethod
    def update(self, message: str) -> None:
        pass