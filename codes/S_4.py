text = input('Enter the text in English: ')
vow = 0
checkThe = 'Предложение не начинается на "The"'
checkEnd = 'не заканчивается на "end"'
length = len(text)
text = text.lower()
for i in range(length):
    if text[i] == 'a' or text[i] == 'e' or text[i] == 'i' or text[i] == 'o' or text[i] == 'u':
        vow += 1
text.replace('ugly', 'beauty')

if text[:3] == 'the':
    checkThe = 'Предложение начинается на "The"'
if text[-4:] == ' end' or text[-5:] == ' end.':
    checkEnd = 'заканчивается на "end"'

print(f'{text}\nДлина предложения - {length}\nГласных "a, e, i, o, u" в тексте - {vow}\n{checkThe} и {checkEnd}.')
