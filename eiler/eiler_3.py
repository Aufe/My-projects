import math
import time
start_time = time.time()
n = 600851475143
lf = []  # list of factors
a = 2

while a ** 2 <= n:
    if n % a == 0:
        lf.append(a)
        lf.append(n // a)
        a += 1
    else:
        a += 1
lf.sort()

print(lf)

lpf = []  # list of prime factors


for i in lf:
    for b in range(2, int(math.sqrt(i) + 1)):
        if i % b == 0:
            break
    else:
        lpf.append(i)


print(lpf)
print(max(lpf))
print("---", time.time() - start_time, "seconds")