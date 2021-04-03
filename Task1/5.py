'''5. В текстовом файле input.txt записан русский текст.
Найти в тексте слова, содержащие подряд какие-нибудь две из четырех наиболее часто встречающихся букв текста,
записать эти слова заглавными буквами и указать после каждого такого слова в скобках найденные буквы.'''

letters='абвгдежзийклмнопрстуфхцчшщъыьэюя'

f = open('input.txt', 'r')
l = str([line.strip() for line in f])
a = str(l.casefold())
words = a.split(" ")

b=list()
for letter in letters:
    b.append(a.count(letter))
b.sort(reverse = True)
b=b[0:4]

for letter in letters:
    if a.count(letter) in b:
        b.append(letter)
Most_often=b[4:8]
print('Наиболее часто встречаются:',Most_often)
print(words)

print(Most_often)
Most = ''.join(Most_often)
for word in words:
    for i in range(3):
        if Most[i]+Most[i+1] in word:
            letters2='('+Most[i]+Most[i+1]+')'
            print(word.upper(),letters2)
