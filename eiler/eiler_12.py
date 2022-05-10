import math
a = 1
i = 0
k = 2
b = []
while len(b) < 250:
    a += k
    b = [el for el in range(1, int(math.sqrt(a+1))) if a % el == 0]
    i += 1
    k += 1
print(a)

