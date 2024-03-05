class MyException(Exception):
    pass


# Функция, которая вызывает исключение, если число не положительно
def positive_number(n):
    try:
        if n <= 0:  # Проверка, является ли число положительным
            raise MyException(f'{n} не является положительным числом')
        print(f'Введено положительное число: {n}')  # Вывод положительного числа
    except MyException as e:
        print(f'Поймано исключение: {e}')  # Вывод информации об исключении


# Функция, которая вызывает исключение, если строка не содержит только цифры
def only_letters(s):
    try:
        if not s.isalpha():  # Проверка, содержит ли строка только буквы
            raise MyException(f'{s} содержит не только буквы')
        print(f'Введена строка только из букв: {s}')  # Вывод строки, состоящей только из букв
    except MyException as e:
        print(f'Поймано исключение: {e}')  # Вывод информации об исключении


# Тестирование функций
test_num = int(input('Введите число: '))
positive_number(test_num)
test_string = input('Введите строку: ')
only_letters(test_string)
