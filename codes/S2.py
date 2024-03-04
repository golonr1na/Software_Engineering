tuples = ['(1, 2, 3), 1)', '(1, 2, 3, 1, 2, 3, 4, 5, 2, 3, 4, 2, 4, 2), 3)', '(2, 4, 6, 6, 4, 2), 9)']


def remove_element(tpl, el):
    lst = list(tpl)
    if el in lst:
        lst.remove(el)
        return tuple(lst)
    else:
        return tpl


for tple in tuples:
    tpl = tuple(map(int, tple[:-4].strip('()').split(',')))
    element = int(tpl[-2:-1][0])
    new_tuple = remove_element(tpl, element)
    print(new_tuple)
