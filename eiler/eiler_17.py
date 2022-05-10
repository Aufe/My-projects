nums = {
    1: "one",
    2: "two",
    3: "three",
    4: "four",
    5: "five",
    6: "six",
    7: "seven",
    8: "eight",
    9: "nine",
    10: "ten",
    11: "eleven",
    12: "twelve",
    13: "thirteen",
    14: "fourteen",
    15: "fifteen",
    16: "sixteen",
    17: "seventeen",
    18: "eighteen",
    19: "nineteen",
    20: "twenty",
    30: "thirty",
    40: "forty",
    50: "fifty",
    60: "sixty",
    70: "seventy",
    80: "eighty",
    90: "ninety",
   }

# one hundred and, one thousand
_1_19 = ""
_1_9 = ""
_20_99 = ""
_101_999 = ""
#sum 99
for i in range(1, 20):
    _1_19 += nums[i]
for i in range(1, 10):
    _1_9 += nums[i]
for i in range(20, 91, 10):
    _20_99 += nums[i] * 10 + _1_9

sum_99 = _1_19 + _20_99
sum_hundred = _1_9 + "hundred" * 9
for i in range(1, 10):
    _101_999 += (nums[i] + "hundredand") * 99 + sum_99

sum_1_1000 = sum_99 + sum_hundred + _101_999 + 'onethousand'
print(len(sum_1_1000))