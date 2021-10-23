k, n = map(int, input().split())
a = list(map(int, input().split()))
ans = 10**14
for start in range(n-1):
    ans = max(sum(a[start:]+a[:start]), ans)
print(ans)
