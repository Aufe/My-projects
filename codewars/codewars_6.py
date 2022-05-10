i = [3, 5, 9, 7, 8]

i_3 = [el for el in i if el % 2 == 0]
i_4 = [el for el in i if el % 2 != 0]
if len(i_3) == 1:
    print(i_3[0])
else:
    print(i_4[0])
