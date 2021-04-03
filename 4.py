a='Дана строка, содержащая русский текст. Если в тексте есть два одинаковых слова, то вывести слова текста в алфавитном поpядке, в противном случае удалить из слов текста гласные буквы.'

a=a.casefold()
b = a.split(" ")
c = a.split(" ")
c.sort()
b.sort()

last_word = ""
for word in b:
    if word != last_word:
        count = [i for i, w in enumerate(b) if w == word]
        print(count)
        if str(len(count))!=1:
            print(c)
            break