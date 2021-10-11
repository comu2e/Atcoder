n = int(input())
ans = 10**14
for i in range(n):
    a,p,x  = list(map(int,input().split()))
    if a < x:
        ans = min(p,ans)
if ans == 10**14:
    print(-1)
else:
    print(ans)