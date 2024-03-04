# Создать текстовый файл “data.txt” и записать в него числа от 1 до 100, каждое на новой строке.
# Затем прочитать этот файл и вывести на экран сумму всех чисел.

with open("data.txt", "w") as f:
    print("Создан файл data.txt")
    for i in range(1, 101):
        f.write(str(i) + "\n")

total = 0
with open("data.txt", "r") as f:
    for line in f:
        total += int(line)

print("Сумма чисел в файле:", total)