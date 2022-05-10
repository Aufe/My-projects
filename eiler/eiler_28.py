n = 1
sum = 1
x = 1
for n in range(2, 1001, 2):
    sum += (x + n) + (x + 2 * n) + (x + 3 * n) + (x + 4 * n)
    x += 4 * n
print(sum)