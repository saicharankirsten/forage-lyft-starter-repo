from abc import ABC, abstractmethod

from engine import engine

class Car(engine,ABC):
    def __init__(self):
        pass
    
    @abstractmethod
    def needs_service(self):
        pass
