x = 1
for i in range(7):
    if x == 6:
        x *= 5
    elif x == 31:
        break
    else:
        x += 1
print(x)
