tuples = ['(1, 2, 3), 8)', '(1, 8, 3, 4, 8, 8, 9, 2), 8)', '(1, 2, 8, 5, 1, 2, 9), 8)']


def find_element(tple, element):
    if tple.count(element) > 0:
        start_index = tple.index(element)
        end_index = tple.index(element, start_index + 1) if tple.count(element) > 1 else ()
        return tple[start_index:end_index + 1] if end_index != () else tple[start_index:]
    else:
        return ()


for tpl in tuples:
    tple = tuple(map(int, tpl[1:-4].strip('()').split(',')))
    element = int(tpl[-2])
    new_tuple = find_element(tple, element)
    print(new_tuple)
