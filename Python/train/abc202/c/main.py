n = int(input())
A = list(map(int,input().split()))
B = list(map(int,input().split()))
C = list(map(int,input().split()))

cnt = [0]*(10**6)
D = [0] *n
for j in range(n):
    D[j] = B[C[j]-1]

for j in range(n):
    cnt[D[j]] += 1

ans = 0
for i in range(n):
    ans += cnt[A[i]]
print(ans)