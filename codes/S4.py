rating = [
    [2, 3, 4, 5, 3, 4, 5, 2, 2, 5, 3, 4, 3, 5, 4],
    [4, 2, 3, 5, 3, 5, 4, 2, 2, 5, 4, 3, 5, 3, 4],
    [5, 4, 3, 3, 4, 3, 3, 5, 5, 3, 3, 3, 3, 4, 4]
]


def correction_grades(grades):
    new_grades = [4 if i == 3 else i for i in grades if i != 2]
    print(f'Исправленные оценки:', *new_grades, sep='\n')


if __name__ == '__main__':
    correction_grades(rating)
