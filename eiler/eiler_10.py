import math
import time

start_time = time.time()
def summaProstihChiselDo(y):
    lpf = [2, 3]
    i = 5
    while i < y:
        for b in range(2, int(math.sqrt(i) + 1)):
            if i % b == 0:
                i += 2
                break
        else:
            lpf.append(i)
            i += 2
    return sum(lpf)


print(summaProstihChiselDo(2000000))
print("time: ", time.time() - start_time)
