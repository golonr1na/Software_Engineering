string = 'Злых людей нет на свете, есть только люди несчастливые.'
simb = input('Буква которую вы ищите: ')
for i in string:
    if i == simb:
        index = string.find(simb)
        print(f"Буква '{simb}' есть в строке под {index} индексом")
        break
else:
    print(f"Буквы '{simb}' нет в указанной строке")