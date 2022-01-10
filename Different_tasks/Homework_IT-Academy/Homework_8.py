import random

"""
Реализовать классы stack и queue, для работы со структурами данных стэк и очередь соответственно. Классы должны поддерживать протокол итерации.
"""

class Stack:
    
    def __init__(self):
        self.__stack = []
    
    def add_element(self, element):
        self.__stack.append(element)
    
    def del_last_element(self):
        self.__stack.pop()
    
    def get_last_element(self):
        try:
            return self.__stack[-1]
        except IndexError:
            pass
    
    def get_size_stack(self):
        return len(self.__stack)
    
    def get_is_empty_stack(self):
        return self.__stack == []
    
    def __iter__(self):
        self.__count = 0
        return self
    
    def __next__(self):
        try:
            while True:
                self.__count -= 1
                return self.__stack[self.__count]
        except IndexError:
            raise StopIteration
    
    size_stack = property(get_size_stack)
    is_empty_stack = property(get_is_empty_stack)


class Queue():
    
    def __init__(self):
        self.__queue = []
    
    def add_element(self, element):
        self.__queue.append(element)
    
    def del_first_element(self):
        try:
            del(self.__queue[0])
        except IndexError:
            pass
    
    def get_last_element(self):
        try:
            return self.__queue[-1]
        except IndexError:
            pass
    
    def get_first_element(self):
        try:
            return self.__queue[0]
        except IndexError:
            pass
    
    def __iter__(self):
        self.__count = -1
        return self
    
    def __next__(self):
        try:
            while True:
                self.__count += 1
                return self.__stack[self.__count]
        except IndexError:
            raise StopIteration

    last_element = property(get_last_element)
    first_element = property(get_first_element)


"""
Реализовать функцию-генератор случайных паролей, пользователь задаёт длинну и возможность включения спец символов.
"""

def gener_symbol(choise):
    symbol = "abcdefghijklmnopqrstuvwxyz"
    numbers = "0123456789"
    if choise == "yes":
        spec_symbol = "`~!@#$%^&*()_+№;:?-=,.<> /\|"
    else:
        spec_symbol = ''
    all = [symbol, symbol.upper(), numbers, spec_symbol]
    all = ''.join(el for el in all)
    while True:
        yield random.choice(all)


def gener_password(l, choise):
    while True:
        a = ''
        for i in gener_symbol(choise):
            a += i
            if len(a) == l:
                break
        yield a

def validation(something):
    while True:
        l = input(f"Please, enter the {something}:\n")
        try:
            l = int(l)
            if l < 1:
                raise RuntimeError("The value is low, enter the number more than 0")
            return l
        except ValueError:
            print("Please, enter an integer number")
            continue
        except RuntimeError as er:
            print(er)
            continue

def password():
    l = validation("password length")
    n = validation("number of passwords")
    choise = input("Do you want that the passwords has special symbol? yes or no?\n")
    p = iter(gener_password(l, choise))
    i = 0
    while i < n:
        print(next(p))
        i += 1

password()