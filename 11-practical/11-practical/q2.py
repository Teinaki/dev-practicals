
# You wrote a singelton-based implementation of a random number generator for
# question 2. Now write a RandomGeneratorPool class. Instead
# of always returning the same instance, maintain a pool of up to three
# instances. 
# The first time we call RandomGeneratorPool(), there aren't any instances so it will
# create one and return it. The second and third time we call it it will also create and
# return new instances. But the fourth time we call it, and every time thereafter, it 
# will just return one of the three instances it has already created.
import random
class RandomGeneratorPool:
    _instances = []
    MAX_INSTANCES = 3

    def __new__(cls):
        if len(cls._instances) < cls.MAX_INSTANCES:
            cls._instances.append(super(RandomGeneratorPool, cls).__new__(cls))
        return random.choice(cls._instances)
    
    def number(self):
        return random.randint(0, 100)

rng = RandomGeneratorPool()
print(f'Random number: {rng.number()}')
rng1 = RandomGeneratorPool()
print(rng is rng1)
