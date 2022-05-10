import math

c = 1
for i in range(3):
    c = c * (6 - i) // (1 + i)
print(c)

x = math.factorial(6) // (math.factorial(3) * math.factorial(6 - 3))
print(x)