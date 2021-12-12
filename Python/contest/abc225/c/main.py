import math
n, m = map(int, input().split())

x = [[0 for i in range(n)] for j in range(m)]
y = [[0 for i in range(n)] for j in range(m)]

B = []
for i in range(n):
    b = list(map(int, input().split()))
    B.append(b)
for i in range(n):
    for j in range(m):
        x[i][j] = (B[i][j]+6)/7
        y[i][j] = (B[i][j]-1) % 7+1


ans = "Yes"
for i in range(n):
    for j in range(m):
        if 0 < i and x[i][j] != x[i-1][j]+1:
            ans = "No"
        elif 0 < j and y[i][j] != y[i-1][j]+1:
            ans = "No"
print(ans)
