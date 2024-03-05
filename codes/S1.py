import time


def timer_decorator(func):
    def wrapper(*args, **kwargs):
        start_time = time.time()
        result = func(*args, **kwargs)
        end_time = time.time()
        print(f'\nФункция была выполнена за {end_time - start_time} сек.')
        return result

    return wrapper


@timer_decorator
def fibonacci():
    fib1 = fib2 = 1
    for i in range(2, 400):
        fib1, fib2 = fib2, fib1 + fib2
        print(fib2, end=' ')


if __name__ == '__main__':
    fibonacci()
