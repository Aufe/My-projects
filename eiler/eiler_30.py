y = 0
for x in range(2, 5*9 ** 5):
    if sum([int(el) ** 5 for el in str(x)]) == x:
        print(x)
        y += x
print(y)