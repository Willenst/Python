'''5. В текстовом файле input.txt записан русский текст.
Найти в тексте слова, содержащие подряд какие-нибудь две из четырех наиболее часто встречающихся букв текста,
записать эти слова заглавными буквами и указать после каждого такого слова в скобках найденные буквы.'''
import re

f = open('input.txt', 'r')
l = str([line.strip() for line in f])
a = str(l.casefold())
a=re.sub('[,.]','',a)
words = a.split(" ")
a=a.replace(' ','')

A = {}

for letter in a:
    A[letter]=A.get(letter,0)+1


P=sorted(A.items(),key=lambda x: x[1])[::-1][0:4]
G=('[{}{}{}{}]'.format(P[0][0],P[1][0],P[2][0],P[3][0]))+'{2}'

print(G)
for word in words:
    if len(re.findall(G,word)):
        print(word.upper()+'('+re.findall(G,word)[0]+')')

