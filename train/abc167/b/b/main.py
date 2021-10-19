a, b, c, k = map(int, input().split())
ans = 0
A = k - a
B = A-b
C = B-c
print(A+B-C)
