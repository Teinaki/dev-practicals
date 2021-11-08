# Implement the RandomNumberGen class as a singelton. It should provide a number() method that returnsxi
# a randomly generated integer.
import random

class RandomNumberGen:
    _instance = None

    def __new__(cls):
        if not cls._instance:
            cls._instance = super(RandomNumberGen, cls).__new__(cls)
        return cls._instance
    
    def number(self):
        return random.randint(0, 100)



rng = RandomNumberGen()
print(f'Random number: {rng.number()}')
rng1 = RandomNumberGen()
print(rng is rng1)

# expected output

# Random number: 42  (Numbers will vary, you know, randomly.)
# True

