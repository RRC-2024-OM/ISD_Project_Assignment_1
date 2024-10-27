"""
Description : Subject handling observer and managing the notifications.
Author : Om Patel
"""
from patterns.observer.observer import Observer

class Subject:
    """Subject is a part of observer design patterns that can attach, detach,
    and notify observer of changes.

    Attributes:
        _observer (list): A list of observer attached to this subject.

    Methods:
        attach(observer): Adds an observer to the list.
        detach(observer): Remove an observer from the list.
        notify(message): Sends a notification to observers.
    """
    def __init__(self) -> None:
        """Initializes the subject with an empty list.
        """
        self._observer = []
    
    def attach(self, observer: Observer) -> None:
        """Attaches an observer to the subject, with allows to receive notifications.

        Args:
            observer (Observer): The observer to attach. 
        """
        self._observer.append(observer)

    def detach(self, observer: Observer) -> None:
        """Detaches an observer from the subject, which ultimately result in stop receiving notifications.

        Args:
            message (str): The observer to detach.
        """
        self._observer.remove(observer)
    
    def notify(self, message: str) -> None:
        """Notify all the attached observers by calling the 'update' with the message.

        Args:
            message (str): The message to send to all observers.
        """
        for observer in self._observer:
            observer.update(message)