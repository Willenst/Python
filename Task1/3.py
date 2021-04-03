'''3. Дана последовательность натуральных чисел {Aj}j=1...n (n<=10000).
 Удалить из последовательности числа, все цифры которых различны, а среди оставшихся продублировать числа-палиндромы.'''

import random

a=[random.randint(0,10000) for i in range(100)]

a=[i for i in a if len(set(str(i)))!=len(str(i))]


for i in range(len(a)):
    if str(int(a[i])) == str(int(a[i]))[::-1]:
        a[i]=(a[i],a[i])
print(str(a).replace('(','').replace(')',''))