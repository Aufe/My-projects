import functools
import time

start_time = time.time()

def evenlyDivisible(n):
    mults = []
    for i in range(1, n + 1):
        currentNum = i
        for element in mults:
            if currentNum % element == 0:
                currentNum = int(currentNum / element)
        mults.append(currentNum)
    return functools.reduce(lambda product, element : product * element, mults, 1)

print(evenlyDivisible(3))
print(time.time() - start_time, "sec")