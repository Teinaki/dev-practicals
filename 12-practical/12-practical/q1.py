# Add code to the cell below that will randomly choose to decorate basic with
# either the ReversingDecorator or the UppercaseDecorator. You may want to
# import random.
import random

from decodemo import ConcreteMessenger, ReversingDecorator, UppercaseDecorator
from decodemo import AbstractDecorator


basic = ConcreteMessenger()
print(basic.say_hello())

# Your code below will create a decorated class and assign it to
# decorated.
decorated = None 

# add your code here 
class RandomDecorator(AbstractDecorator):
    def __init__(self, messenger):
        self._messenger = messenger
        decorator = random.choice([ReversingDecorator, UppercaseDecorator])
        self._decorated = decorator(self._messenger)

    def say_hello(self):
        return self._decorated.say_hello()

    def say_goodbye(self):
        return self._decorated.say_goodbye()
        
decorated = RandomDecorator(basic)


print(decorated.say_hello())    
