n = int(input())
A = list(map(int,input().split()))
B = list(map(int,input().split()))
ans = 0
setAns = [i for i in range(1,1001)]
minA = min(A)
maxB = max(B)
maxSet = set([i for i in range(minA,maxB+1)])
for a in A:
    for b in B:
        setX = set([i for i in range(min(a,b+1),max(a,b+1))])
        maxSet = setX & maxSet
print(len(maxSet))