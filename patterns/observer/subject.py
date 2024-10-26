"""
Description : Subject handling observer and managing the notifications.
Author : Om Patel
"""
from patterns.observer.observer import Observer

class Subject:
    def __init__(self) -> None:
        self._observer = []
    
    def attach(self, observer: Observer) -> None:
        self._observer.append(observer)

    def detach(self, observer: Observer) -> None:
        self._observer.remove(observer)
    
    def notify(self, message: str) -> None:
        for observer in self._observer:
            observer.update(message)