def plus(x, y):
    return x + y

def minus(x, y):
    return x - y

def times(x, y):
    return x * y

def divided(x, y):
    return x / y


operators = {
    "+": [1, plus],
    "-": [1, minus],
    "*": [2, times],
    "/": [2, divided]
}


