b = 0
for i in range(13, 1, -1):
    a = []
    k = i
    a.append(k)
    
    while k != 1:
        if k % 2 == 0:
            k = k // 2
            a.append(k)
        else:
            k = 3 * k + 1
            a.append(k)
    
    if len(a) > b:
        b = len(a)
        d = i


print(d)