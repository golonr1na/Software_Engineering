def fib(n):
    a, b = 1, 1
    count = 0
    with open('fib.txt', 'w') as txt:
        while count < n:
            yield a
            a, b = b, a + b
            txt.write(str(a) + '\n')
            count += 1


print(*[i for i in fib(200)])
