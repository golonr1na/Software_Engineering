nums = input('Нажмите ладонью на numpad один раз\n')


def count_numbers(string):
    num_freq = {}

    for i in string:
        i = int(i)
        num_freq[i] = num_freq.get(i, 0) + 1

    sorted_num_freq = sorted(num_freq.items(), key=lambda item: item[1])
    top_three = dict(sorted(sorted_num_freq[-3:]))
    return top_three


print(count_numbers(nums))
