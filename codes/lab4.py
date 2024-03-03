def main(x, *args):
    one = x
    two = sum(args)
    three = float(len(args))
    print(f'one={one}\ntwo={two}\nthree={three}')
    return x + sum(args) / float(len(args))

if __name__ == '__main__':
    result = main(14, 1, -4, 2, 6, -9, 0, 7, 4)
    print(f'\nresult={result}')
