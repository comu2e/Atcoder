a,b,c,d = list(map(int,input().split()))

cnt = 0
for i in range(1,10**5+1):
    a += b
    if a <= i*c*d:
        cnt = i
        break
if cnt == 0:
    print(-1)
else:
    print(cnt)