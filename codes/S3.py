from math import sqrt

list = [[12, 25, 3, 48, 71], [5, 18, 40, 62, 98], [4, 21, 37, 56, 84]]
max_triangle = []
min_triangle = []


def count_area(a, b, c):
    p = (a + b + c) / 2
    s = sqrt(p * (p - a) * (p - b) * (p - c))
    return s


for partOfList in list:
    max_triangle.append(max(partOfList))
    min_triangle.append(min(partOfList))

print(f'S наибольшего равна {count_area(*max_triangle)}\nS наименьшего равна {count_area(*min_triangle)}')
