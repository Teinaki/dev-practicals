# For this question you will write a function decorator that takes an integer
# argument. This decorator should be applicable to functions that return
# integers. Your decorator will produce a function that takes the original
# functions return value, multiply it by the value supplied as an argument to
# the decorator, and return that. Don't forget to handle possible arguments
# to the decorated function.
import random
from abc import ABC, abstractmethod
class AbstractInteger(ABC):
    """The abstract base class defines our messenger interface and
    is the base of all our following classes. Note that any concrete
    subclasses must override any methods marked as abstract.
    """
    @abstractmethod
    def return_integer(self):
        pass
class ConcreteInteger(AbstractInteger):
    """This class must implement the thee abstract methods in its parent."""
    def __init__(self, element):
        self._element = element

    def return_integer(self):
        return self._element
     
class DecoratorInteger(AbstractInteger):
    def __init__(self, element):
        self._element = element

    def return_integer(self, element):
        return self._element.return_integer() * element
        
basic = ConcreteInteger(2)
print(basic.return_integer())

decorated = DecoratorInteger(basic)
print(decorated.return_integer(6))    