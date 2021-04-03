
n = 20
m = 20
a = [[0] * m] * n
for i in range(20):
    for j in range(20):
        a[i][j]=j+1
a2=0
for i in range (20):
    a1=max(a[i])
    a2+=a1
print(a2)