a = "asdfads"
k = 2
d =[]
b = [el for el in a]

while len(b) % k != 0:
    b.append("_")

for i in range(0 ,len(b) - k + 1, k):
    c = "".join(b[i:i + k])
    d.append(c)
print(d)


a = "sadasdasdfgdfgk"

if len(a) % 2 == 1:
    a += "_"
print([a[i:i+2] for i in range(0, len(a), 2)])