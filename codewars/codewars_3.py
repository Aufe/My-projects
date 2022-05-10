import math
a = int(input('Please write number: '))
b = []

for i in range(2, int(math.sqrt(a) + 1)):
    if a % i == 0:
        b.append(i)
        b.append(a // i)
        b = set(b)
        b = list(b)
        b.sort()

if len(b) == 0:
    a = str(a)
    print(a + ' is prime')
else:
    print(b)
