lists = [[1, 1, 3, 3, 1], [5, 5, 5, 5, 5, 5, 5], [2, 2, 1, 2, 2, 5, 6, 7, 1, 3, 2, 2]]


def convert_to_set(list, setl):
    for i in range(len(list)):
        if list[:i + 1].count(list[i]) != 1:
            setl.add(str(list[i]) * list[:i + 1].count(list[i]))
    return setl


for l in lists:
    setl = set(l)
    print(convert_to_set(l, setl))
