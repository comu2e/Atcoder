import math
n = int(input())
a = list(map(int,input().split()))

ans = -10**2
gcdCount = []

for i in range(2,max(a)+1):
    gcdList = list(map(lambda el :math.gcd(i,el),a))
    countI = gcdList.count(i)

    gcdCount.append([i,countI])

sorted_gcd = sorted(gcdCount,key=lambda x:x[1],)
print(sorted_gcd[-1][0])