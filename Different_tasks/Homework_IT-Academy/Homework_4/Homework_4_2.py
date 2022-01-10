"""
Написать программу для вычисления суммы долга при расчёте в ресторане. 
Например, счёт в 150$ делится на троих, участник №1 внёс 100$, двое остальных (№2 и №3) - 15$ и 35$ соответственно. 
Программа должна оповестить пользователя о том, что участник №2 должен участнику №1 ещё 35$, а участник №3 - ещё 15$.
"""

import decimal

def validation(x, y):
    while True:
        n = input()
        try:
            if y == "int":
                n = int(n)
            else:
                n = decimal.Decimal(n)
            if n < x:
                raise TimeoutError("Please, enter the correct number")
            return n
        except ValueError:
            print("Please, enter the correct number")
            continue
        except decimal.InvalidOperation:
            print("Please, enter the correct number")
            continue
        except TimeoutError as er:
            print(er)
            continue


def rest():
    l = []
    num = 1
    print("How many people pay in the restaurant?")
    n = validation(1, "int")
    while len(l) < n:
        print(f"How did the pay {num} person?")
        cash = validation(0, "decimal")
        l.append(round(cash, 2))
        num += 1
    return l

def owes(l):
    if max(l) - min(l) <= 0.01:
        return
    else:
        delta_min = cash_1_person - min(l)
        delta_max = max(l) - cash_1_person
        z = min(delta_min, delta_max)
        print(f"{l.index(min(l)) + 1} owes {round(z, 2)}$ to {l.index(max(l)) + 1}") 
        l[l.index(min(l))] = min(l) + z
        l[l.index(max(l))] = max(l) - z
        return owes(l)

l = rest()
cash = sum(l)
cash_1_person = cash / len(l)

owes(l)