list = [3, 6, 8, 12, 51, 60]
flag = False
for i in list:
    if i % 2 != 0:
        flag = True
        break

if flag is True:
    print('В массиве есть нечетное число')
else:
    print('В массиве все числа четые')