'''2. Дана целочисленная матрица {Aij}i=1,...,n;j=1,...,m (n,m<=20).    Найти сумму максимальных элементов строк.'''
n,m = 5,5
a=list(list(i for i in range(1,m+1)) for j in range(1,n+1))
print(sum(map(max,zip(*a))))


