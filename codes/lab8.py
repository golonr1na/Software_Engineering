num = 0
while num < 10:
    num += 3
    if num % 2 == 0:
        print(f'Число {num} четное')
    elif num > 10:
      break
    else:
        print(f'Число {num} нечетное')
        num -= 1

