"""
Дан список вида ['1', '11', '12', '22', '2', '13', '30', '33'].
Отсортировать его по возрастанию числовых значений, исключив те, квадраты которых являются чётными числами.
Программа должна занимать одну строчку.
"""

def sort_list(l):
    '''
    This function sorts a list.

    l: list
    return: list

    '''
    return sorted(filter(lambda x : int(x) % 2 != 0, l), key=lambda x : int(x))

# l = ['1', '11', '12', '22', '2', '13', '30', '33', '315']
# print(sort_list())

"""
Написать функцию для вычисления суммы всех элементов вложенных (любая глубина) списков.
Пример списка (синтаксис Python): [1, 2, [2, 4, [[7, 8], 4, 6]]], сумма элементов - 34
"""

def sum_list(l, sum = 0):
    '''
    This function summ the elements in the list.

    l: list
    return: sum

    '''
    for el in l:
        if type(el) == list:
            sum = sum_list(el, sum)
        else:
            sum += el
    return sum 

# l = [1, 2, [2, 4, [[7, 8], 6, 8, 9, [6, [2, 3]], [4, 6]]]]
# print(sum_list(l))

"""
Написать функцию для вычисления суммы n первых чисел Фибоначчи
"""

def sum_n_fib(n, a = 0, b = 1):
    '''
    This function summ the first n numbers of the Fibonacci sequence.

    n: int
    return: int

    '''
    if n == 1:
        return 0
    else:
        a, b = b, a + b
        return a + sum_n_fib(n - 1, a, b)

# print(sum_n_fib(87))