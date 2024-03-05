# Определение класса-декоратора my_decorator
class my_decorator:
    # Инициализация метода конструктора с функцией func
    def __init__(self, func):
        self.func = func

    # Определение метода call, который будет вызываться при применении декоратора к функции
    def __call__(self, *args, **kwargs):
        print(f'Декоратор до выполнения функции "{self.func.__name__}"')  # Вывод сообщения перед выполнением функции
        result = self.func(*args, **kwargs)  # Выполнение функции с переданными аргументами
        print(f'Декоратор после выполнения функции "{self.func.__name__}"')  # Вывод сообщения после выполнения функции
        return result


# Декорирование функций addition и multiply с помощью декоратора my_decorator
@my_decorator
def addition(a, b):
    return a + b  # сложение входящих аргуметов


@my_decorator
def multiply(a, b):
    return a * b  # умножение входящих аргуметов


# Запрос у пользователя двух чисел для выполнения операций
x = int(input('Введите первое число: '))
y = int(input('Введите второе число: '))

# Вызов функций addition и multiply с введенными числами в качестве аргументов
print(addition(x, y))
print(multiply(x, y))
