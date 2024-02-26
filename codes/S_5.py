string = 'hello'
memory = ' world'
values = [0, 2, 4, 6, 8, 10]
counter = 0
while counter != 10:
    if counter in values:
        print(string + memory)
        print(string)
    counter += 1
string = string + ' world'
memory = string
print(memory)