from abc import ABC, abstractmethod

class Command(ABC):
    @abstractmethod
    def execute(self): pass

class OperationCommand(Command):
    def __init__(self, operation, a, b):
        self.operation = operation
        self.a = a
        self.b = b

    def execute(self):
        return self.operation.execute(self.a, self.b)