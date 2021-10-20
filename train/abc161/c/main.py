n, k = map(int, input().split())
x = n

x = min(abs(x % k-k), x % k)
print(x)
