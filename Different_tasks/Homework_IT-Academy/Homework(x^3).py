"""
a * x ** 3 + b * x ** 2 + c * x + d = 0
"""


import math
a = float(input("Введите a:"))
b = float(input("Введите b:"))
c = float(input("Введите c:"))
d = float(input("Введите d:"))

def x(y):
    x = y - b / (3 * a)
    return x

#y ** 3 + p * y + q = 0

p = (3 * a * c - b ** 2) / (3 * a ** 2)
q = (2 * b **3 - 9 * a * b * c + 27 * a ** 2 * d) / (27 * a ** 3)
Q = (p / 3) ** 3 + (q / 2) ** 2

if Q == p == q == 0: # 3 равных корня
    y_1, y_2, y_3 = 0, 0, 0
elif Q >= 0:
    if -q / 2 + math.sqrt(Q) < 0:
        alfa = -math.fabs(-q / 2 + math.sqrt(Q)) ** (1 / 3)
    else:
        alfa = (-q / 2 + math.sqrt(Q)) ** (1 / 3)
    if -q / 2 - math.sqrt(Q) < 0:
        beta = -math.fabs(-q / 2 - math.sqrt(Q)) ** (1 / 3)
    else:
        beta = (-q / 2 - math.sqrt(Q)) ** (1 / 3)
    if Q > 0: # 1 вещ + 2 комплекс
        y_1 = alfa + beta
        y_2 = complex(-(alfa + beta) / 2, (alfa - beta) * math.sqrt(3) / 2)
        y_3 = complex(-(alfa + beta) / 2, (alfa - beta) * math.sqrt(3) / 2)
    elif Q == 0: # 3 вещ корня (из которых 2 одинаковые)
        y_1 = 2 * alfa
        y_2 = y_3 = -alfa
else: # 3 разных вещ корня
    y_1 = 2 * math.sqrt(-p / 3) * math.cos(math.acos((-q / 2) * (3 / -p) ** (3 / 2)) / 3)
    y_2 = 2 * math.sqrt(-p / 3) * math.cos(math.acos((-q / 2) * (3 / -p) ** (3 / 2)) / 3 + 2 * math.pi / 3)
    y_3 = 2 * math.sqrt(-p / 3) * math.cos(math.acos((-q / 2) * (3 / -p) ** (3 / 2)) / 3 - 2 * math.pi / 3)
print("x_1 =", x(y_1))
print("x_2 =", x(y_2))
print("x_3 =", x(y_3))