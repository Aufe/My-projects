"""
Реализовать функцию get_ranges которая получает на вход непустой список неповторяющихся целых чисел, 
отсортированных по возрастанию, которая этот список “сворачивает”.
"""

l = [0, 2, 3, 4, 5, 6, 7, 10, 11, 12, 13, 15, 16, 18, 22, 32, 34, 35, 36]
num = 0

def create(l_new):
    if len(l_new) == 1:
        return l_new[0]
    else:
        return f"{l_new[0]}-{l_new[-1]}" 

def get_l_new(l):
    global num
    l_new = []
    l_new.append(l[0])
    for el in range(1, len(l)):
        if l[el] - 1 == l_new[-1]:
            l_new.append(l[el])
        else:
            num += len(l_new)
            break
    else:
        num += len(l_new)
    return l_new

def get_ranges(l):
    a = []
    while num < len(l):
        l_short = l[num:]
        a.append(create(get_l_new(l_short)))
    return ", ".join(str(el) for el in a)

print(get_ranges(l))