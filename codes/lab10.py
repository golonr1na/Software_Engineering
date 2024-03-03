global result


def rectangle(a, b):
    global result
    result = a * b


def triangle(a, h):
    global result
    result = 0.5 * a * h


figure = input("1-прямоугольник, 2-треугольник:")

if figure == '1':
    rectangle(a=float(input("Ширина: ")), b=float(input("Высота: ")))
elif figure == '2':
    triangle(a=float(input("Основание: ")), h=float(input("Высота: ")))

print(f"Площадь: {result}")
