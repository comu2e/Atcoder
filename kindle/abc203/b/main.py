n,k = map(int,input().split())

ans = 0

for i in range(1,n+1):
    for j in range(1,k+1):
        room = 100*i + j
        ans += room
print(ans)