
n,k = map(int,input().split())

def g1(x):
    listx = list(str(x))
    listx.sort(reverse=True)
    return  int("".join(listx))
def g2(x):
    listx = list(str(x))
    listx.sort()
    return  int("".join(listx))

inita = n

for i in range(1,k+1):
    inita = g1(inita) - g2(inita)
print(inita)