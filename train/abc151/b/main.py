n, k, m = map(int, input().split())
A = list(map(int, input().split()))

for i in range(k+1):
    sumA = sum(A) + i
    if sumA / n >= m:
        print(i)
        exit()
print(-1)
