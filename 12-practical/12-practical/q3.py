# Write a Python function decorator that implements the UppercaseDecorator
# idea from demodeco.py. In this case, though, it doesn't wrap an entire
# class, it just can decorate any function that returns a string. This new
# version has an added twist: Using something like a pseudorandom number,
# only uppercase the return value about half the time.
# Include an if __name__ == '__main__' block that demonstrates the use of your decorator.
import random

from decodemo import ConcreteMessenger, UppercaseDecorator
from decodemo import AbstractDecorator

class RandomDecorator(AbstractDecorator):
    def __init__(self, messenger):
        self._messenger = messenger
        self.rand = random.choice([0, 1])
        if self.rand == 0:
            self._decorated = UppercaseDecorator(self._messenger)
        else:
            self._decorated = self._messenger

    def say_hello(self):
        return self._decorated.say_hello()

    def say_goodbye(self):
        return self._decorated.say_hello()
        

def main():
    basic = ConcreteMessenger()
    decorated = RandomDecorator(basic)

    print(decorated.say_hello())

if __name__ == '__main__':
    main()

