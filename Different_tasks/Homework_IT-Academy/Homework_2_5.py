"""
Пользователь вводит две строки - str1 и str2

1. Проверить, равны ли данные строки (str1 == str2 запрещено)

2. Проверить, является ли str2 подстрокой str1 (str2 in str1 запрещено)

3. Проверить, является ли str1 полиндромом
"""

str1 = input("Enter str1, please:\n")
str2 = input("Enter str2, please:\n")

if len(str1) == len(str2):
    for i in range(len(str1)):
        if str1[i] != str2[i]:
            print("str1 != str2")
            break
    else:
        print("str1 == str2")
else:
    print("str1 != str2")
    if len(str1) > len(str2):
        i = 0
        j = 0
        while i < len(str2) and j <= len(str1) - len(str2):
            if str2[i] == str1[j + i]:
                i += 1
            else:
                i = 0
                j += 1
        else:
            if i == len(str2):
                print("str2 является подстрокой str1")
            else:
                print("str2 не является подстрокой str1")
    else:
        print("str2 не является подстрокой str1")

if str1 == str1[::-1]:
    print("str1 - palindrome")
else:
    print("str1 - not palindome")