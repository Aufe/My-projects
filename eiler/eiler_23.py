import itertools
a = []
for i in range(28123):
    sum_divisors = 0
    for el in range(1, i // 2 + 1):
        if i % el == 0:
           sum_divisors += el
    if sum_divisors > i:
        a.append(i)
print(a)
x = 0
b = set(sum(j) for j in itertools.combinations_with_replacement(a, 2) if sum(j) < 28123)
for el in range(28123):
    if el not in b:
        x += el
print(x)