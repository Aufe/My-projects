import math

a = sum(int(el) for el in str(math.factorial(100)))
print(a)

def fact(x):
    if x == 1:
        return x
    return x * fact(x - 1)

print(fact(3))