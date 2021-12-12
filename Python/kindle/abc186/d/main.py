n = int(input())
a = list(map(int,input().split()))
a.sort()
ans = 0
sm = sum(a)

for i in range(n-1):
    ans += sm
    sm -=a[i]
    ans -= (n-i)*a[i]
print(ans)