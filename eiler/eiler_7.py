import math


def prostoeChisloNomer(y):
    lpf = [2, 3]
    x = len(lpf)
    i = 5
    while x < y:
        for b in range(2, int(math.sqrt(i) + 1)):
            if i % b == 0:
                i += 2
                break
        else:
            lpf.append(i)
            x = len(lpf)
            i += 2
    return max(lpf)

print(prostoeChisloNomer(500))