"""
Реализовать:
1.текстовый вывод текущего времени
2.текстовый вывод времени, введённого с консоли (hh:mm).

Для получения текущего времени использовать модуль datetime.

min < 30: столько-то минут следующего часа
min == 30: половина такого-то
min > 30 and min < 45 столько-то минут следующего часа
min >= 45 без min такого-то
"""

import datetime

while True:
    random_time = input("Enter your time in format 'hh:mm', please:\n")
    random_hour = int(random_time.split(":")[0])
    random_minute = int(random_time.split(":")[1])
    if 0 <= random_hour <= 24 and 0 <= random_minute <= 59:
        break
    else:
        print("Incorrect input, try again.")

minutes = {
    1: "одна",
    2: "две", 
    3: "три",
    4: "четыре",
    5: "пять",
    6: "шесть",
    7: "семь",
    8: "восемь",
    9: "девять",
    10: "десять",
    11: "одиннадцать",
    12: "двенадцать",
    13: "тринадцать",
    14: "четырнадцать",
    15: "пятнадцать",
    16: "шестнадцать",
    17: "семнадцать",
    18: "восемнадцать",
    19: "девятнадцать",
    20: "двадцать",
    30: "тридцать",
    40: "сорок",
    45: "пятнадцати",
    46: "четырнадцати",
    47: "тринадцати",
    48: "двенадцати",
    49: "одиннадцати",
    50: "десяти",
    51: "девяти",
    52: "восьми",
    53: "семи",
    54: "шести",
    55: "пяти",
    56: "четырех",
    57: "трех",
    58: "двух",
    59: "одной"
}

hours_45_59 = {
    0: "час",
    1: "два",
    2: "три",
    3: "четыре",
    4: "пять",
    5: "шесть",
    6: "семь",
    7: "восемь",
    8: "девять",
    9: "десять",
    10: "одиннадцать",
    11: "двенадцать",
}

hours_1_44 = {
    0: "первого",
    1: "второго",
    2: "третьего",
    3: "четвертого",
    4: "пятого",
    5: "шестого",
    6: "седьмого",
    7: "восьмого",
    8: "девятого",
    9: "десятого",
    10: "одиннадцатого",
    11: "двенадцатого",
}

end_min = {
    "ь": "минут",
    "а": "минута",
    "е": "минуты",
    "и": "минуты",
    "к": "минут"
}

end_hour = {
    "ь": "часов",
    "а": "часа",
    "и": "часа",
    "е": "часа"
}

current_hour = datetime.datetime.now().hour
current_minute = datetime.datetime.now().minute

def cur_time_in_words(hour, minute):
    if hour > 12 or (hour == 12 and minute != 0):
        hour = hour - 12
    if hour == 0 and minute == 0:
        return "Полночь."
    elif hour == 12 and minute == 0:
        return "Полдень."
    elif minute == 0:
        if hour == 1:
            return "Ровно {}.".format(hours_45_59[hour - 1])
        else:
            return "Ровно {} {}.".format(hours_45_59[hour - 1], end_hour[hours_45_59[hour - 1][-1]])
    elif minute == 30:
        return "Половина {}.".format(hours_1_44[hour])
    elif 0 < minute < 45:
        if 1 <= minute <= 20 or minute == 40:
            return "{} {} {}.".format(minutes[minute], end_min[minutes[minute][-1]], hours_1_44[hour]).capitalize()
        else:
            return "{} {} {} {}.".format(minutes[minute - minute % 10], minutes[minute % 10], end_min[minutes[minute % 10][-1]], hours_1_44[hour]).capitalize()
    else:
        return "Без {} {}.".format(minutes[minute], hours_45_59[hour])

print("Time now: ", cur_time_in_words(current_hour, current_minute))
print("Your time: ", cur_time_in_words(random_hour, random_minute))

