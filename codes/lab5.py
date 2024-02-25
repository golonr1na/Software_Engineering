for i in range(10):
    print(f"i = {i}")
    if i == 0:
        i += 2
    if i == 1:
        continue
    if i == 2 or i == 3:
        print('Переменная равна 2 или 3')
    elif i in [6, 8, 9]:
        print('Переменная равна 6, 8 или 9')
    else:
        break