a,b = map(int,input().split())
c,d = map(int,input().split())

ans = []
for x in range(a,b+1):
    for y in range(c,d+1):
        ans.append(x-y)
print(max(ans))