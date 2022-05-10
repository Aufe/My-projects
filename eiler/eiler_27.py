import math

def is_prime(test):
    prime = True
    if test < 2:
        return False
    if test == 2:
        return True
    for i in range(2, int(math.sqrt(test) + 1)):
        if test % i == 0:
            prime = False
            break
    return prime
    
y_max = 0
for a in range(-999, 1000):
    for b in range(-1000, 1001):
        n = 0
        while True:
            x = n ** 2 + a * n + b
            if is_prime(x):
                n += 1
            else:
                break
        if n > y_max:
            y_max = n
            k_a = a
            k_b = b

print("y_max =", y_max, "k_a =", k_a, "k_b =", k_b)
print(k_a * k_b)