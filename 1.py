def test(x):
    suma=0
    while x!=0:
        suma+=x%10
        x=x//10
    if suma==14:
        return True



a=[i for i in range(1,10001)]
if any(test(i)==True for i in a):
    a=a[::-1]
print(a)
