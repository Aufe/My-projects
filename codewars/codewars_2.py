def doubleCod(number):
    a = str()
    b = 0
    while number // 2 != 0:
        if number % 2 == 0:
            a += '0'
        else:
            a += '1'
        number = number // 2
    else: a += '1'
    print(a[::-1])

    for i in a:
        if i == '1':
            b += 1
    print(b)


doubleCod(int(input('Please write number: ')))
