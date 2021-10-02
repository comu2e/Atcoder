import itertools

n = int(input())
a = list(map(int,input().split()))

maxN10 = 2**(n-1) -1
cnt = 0
resList = []
for i in range(maxN10):

    binI = bin(i)
    res = 0
    fg_array = str(binI[2:]).ljust(n-1, '0')
    
    for k,fg in enumerate(fg_array):
        print(res)
        print("----")
        if fg == "0":
            res += res * a[k]
        if fg == "1":
            res += res * a[k]
    res = res % 10
    print("_____")
    resList.append(res)
    
for j in range(10):
    print(resList.count(j))