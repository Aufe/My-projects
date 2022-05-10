from fractions import gcd
from functools import reduce

print('Это число', reduce(lambda a, b: (a * b) / gcd(a, b), range(1, 20), 1))
