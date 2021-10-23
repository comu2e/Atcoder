n, k = map(int, input().split())
i = 0
cnt = 1
while n > 0:
    for j in k:
        n -= k*k**i
        cnt += 1
print(cnt)
