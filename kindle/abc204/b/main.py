n = int(input())
a = list(map(int,input().split()))

ans = 0

for i in a:
    if i <= 10:
        pass
    else:
        ans += i -10
print(ans)