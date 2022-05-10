y = 0
for i in range(2, 1000):
    x = 1
    z = i
    if z % 2 == 0:
        z = z // 2
    elif z % 5 == 0:
        z = z // 5
    else:
        while 10 ** x % z != 1:
            x += 1
        else:
            print("i =", i, "x =", x)
            if x > y:
                y = x
                max_i = i
print(y)
print(max_i)