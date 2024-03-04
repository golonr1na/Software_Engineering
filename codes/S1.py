numbers = input('Введите числа через пробел: ')
lst = numbers.split()
tpl = tuple(lst)
print(lst, tpl, sep='\n')
