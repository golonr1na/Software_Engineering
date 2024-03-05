def sum_num():
    try:
        num = float(input('Введите число: \n'))
        res = num + 2
        return res
    except ValueError:
        return 'Неподходящий тип данных. Ожидалось число.'

print(sum_num())
print(sum_num())

