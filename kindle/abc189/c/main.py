n = int(input())
a = list(map(int,input().split()))

res = -10**15

for l in range(n):
    a_min = a[l]
    for r in range(l,n):
        a_min = min(a_min,a[r])
        tempRes = (r-l+1) * a_min
        res = max(tempRes,res)
print(res)