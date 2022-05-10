sum_x = 0
for x in range(1, 10000):
    def sum_divisors(x):
        sum = 0
        for i in range(1, x // 2 + 1):
            if x % i == 0:
                sum += i
        return sum
    if sum_divisors(sum_divisors(x)) == x and sum_divisors(x) < 10000 and x != sum_divisors(x):
        sum_x += x
print(sum_x)