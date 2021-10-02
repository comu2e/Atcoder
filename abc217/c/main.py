n = int(input())
P = list(map(int, input().split()))
Q = [0]*n
cnt = 0
for i in P:
  cnt += 1
  Q[i-1] = cnt
print(*Q)


