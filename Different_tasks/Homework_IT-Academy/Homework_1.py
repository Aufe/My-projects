'''Депозит:
начальная сумма - 20000 BYN
срок - 5 лет
процент (годовой) - 15%
ежемесячная капитализация


Вычислить сумму на счету в конце указанного срока.'''

import decimal

cash = 20000
dep_time = 5
percent = 15

new_cash = cash * (1 + decimal.Decimal(percent)/100/12) ** (dep_time * 12)

print("Сумма на счету через 5 лет: ", round(new_cash, 2), " BYN")