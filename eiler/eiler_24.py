import itertools

a = "0123456789"
b = [el for el in itertools.permutations(a)]
x = ""
for i in b[999999]:
    x += i
print(x)
print(len(b))