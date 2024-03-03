def main(**kwargs):
    for i in kwargs.items():
        print(i[0], i[1])
    print()
    for key in kwargs:
        print(f"{key} = {kwargs[key]}")

if __name__ == '__main__':
    main(x=[1, 0, 3], y=[5, 3, 0], z=[2, 3, 4], q=[6, 3, 0], w=[3, 8, 0])
    print()
    main(**{'x': [1, 0, 3], 'y': [5, 3, 0]})