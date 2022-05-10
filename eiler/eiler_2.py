a = 1
b = 2
sum = 0

while b <= 4E6:
    if b % 2 == 0:
        sum = sum + b
    c = a
    a = b
    b = c + b

print(sum)
