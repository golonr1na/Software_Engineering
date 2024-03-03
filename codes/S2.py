import random


def dice():
    roll = random.randrange(1, 6)
    print(f'Выпало - {roll}')
    if roll >= 5:
        print('Вы победили')
    elif 3 <= roll <= 4:
        dice()
    elif 1 <= roll <= 2:
        print('Вы проиграли')


if __name__ == '__main__':
    dice()
