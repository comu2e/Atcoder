import math
n,x = map(int,input().split())

sum_alchol = 0
cnt = 1
for i in range(n):
    v,p = map(int,input().split())
    sum_alchol += v*p
    if sum_alchol > 100*x:
        print(cnt)
        break
    else:
        cnt += 1
if cnt == n+1:
    print(-1)