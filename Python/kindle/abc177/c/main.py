n = int(input())
a = list(map(int,input().split()))
mod = 10**9+7

res = 0
a_sum = sum(a)
for i in range(n):
    a_sum -= a[i]
    res += a[i]*a_sum
    res %= mod
print(res)
    