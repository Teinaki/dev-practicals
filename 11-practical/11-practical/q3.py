# Write a module-based implementation of the RandomNumberGen class like the one you wrote for q1, based
# on the last example in 10-patterns-singletons.md. Then write a second file,
# singelton_client.py that imports your q3 module and demonstrates its use.
import random

class _RandomNumberGen:
    _instance = None

    def __new__(cls):
        if not cls._instance:
            cls._instance = super(_RandomNumberGen, cls).__new__(cls)
        return cls._instance
    
    def number(self):
        return random.randint(0, 100)

randomNumberGen = _RandomNumberGen()

class RandomNumberGen:
    def __new__(cls):
        return randomNumberGen