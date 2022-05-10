def fibon(x):
    a = [1, 1]
    z = 2
    while len(str(a[1])) < x:
        a[0], a[1] = a[1], a[0] + a[1]
        z += 1
    return(z)

print(fibon(1000))