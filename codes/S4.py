def mean(data):
    return sum(data) / float(len(data))


def main(**kwargs):
    for i, j in kwargs.items():
        print(f"{i}) Среднее арифметическое = {mean(j)}")


if __name__ == '__main__':
    main(
        a=[2, 8, 6],
        b=[3, 5, 7, 9]
    )
