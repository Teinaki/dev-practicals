# randrange(1, 101) returns random numbers between 1 and 100. Using partial,
# produce a function highrange so that highrange(101) produces values from
# 70 to 100.

from random import randrange
from functools import partial

# Write your solution below.
def high(x, y):
    return randrange(x,y)

rand_num = randrange(1,101)
highrange = partial(high, 70)
print(f'Random number: {rand_num}')
print(f'High Range Random number: {highrange(101)}')