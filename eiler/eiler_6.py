def raznost(x):
    a = 0
    b = 0
    for i in range(1, x + 1):
        n = i ** 2
        a += n
        b += i
    c = b ** 2
    d = c - a
    return d

print(raznost(1000))