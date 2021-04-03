'''3. Дана последовательность натуральных чисел {Aj}j=1...n (n<=10000).
 Удалить из последовательности числа, все цифры которых различны, а среди оставшихся продублировать числа-палиндромы.'''


def right(x):
    if x<10:
        return True
    while x!=0:
        x1=x%10
        x = x // 10
        while x!=0:
            x2=x%10
            x=x//10
            if x1==x2:
                return True

def polindrom(x):
    x1=str(x)
    if x1==x1[::-1]:
        return True



a=[i for i in range(1,10001) if right(i)==True]
b=a[:]
for i in a:
    if polindrom(i)==True:
        b.append(i)


print(b)