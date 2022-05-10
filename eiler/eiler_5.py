import time

x = 20
i = 2
start_time = time.time()
while i < 21:
    if x % i == 0:
        i += 1
    else:
        x += 20
        i = 2


print(x)
print(time.time() - start_time, "sec")
