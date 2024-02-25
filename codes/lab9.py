list = []
n = 0
for i in range(4):
    for j in range(4):
        list.append(f'{i} {j}')
        if i != j:
            n += 1
        else:
            pass

print(f"{list}\nЭлементов в списке {len(list)}. Не совпадающих {n}")