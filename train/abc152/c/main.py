n = int(input())
P = list(map(int, input().split()))
cnt = 0
mi = 10**15
for i in range(n):
    mi = min(mi, P[i])
    if mi == P[i]:
        cnt += 1
print(cnt)
