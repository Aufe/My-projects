import time
start_time = time.time()
x = 0
for a in range(100, 1000):
    for b in range(100, 1000):
        c = a * b
        c_str = str(c)
        if c_str == c_str[::-1]:
            if int(c_str) > x:
                x = int(c_str)

print(x)

print("---", time.time() - start_time, "seconds")
