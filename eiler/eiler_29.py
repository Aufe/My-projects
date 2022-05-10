my_set = set()
for a in range(2, 101):
    for b in range(2, 101):
        my_set.add(a ** b)

print(len(my_set))