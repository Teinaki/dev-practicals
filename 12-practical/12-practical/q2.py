# Define your own decorator class, SilentDecorator that inherits from
# AbstractDecorator in decodemo.py. This decorator shall modify the behaviour
# of any methods returning strings so that they return empty strings. Methods
# that do not return strings should return their ususal values.
from decodemo import AbstractDecorator

class SilentDecorator(AbstractDecorator):
    def say_hello(self):
        return ''
    def say_goodbye(self):
        return ''