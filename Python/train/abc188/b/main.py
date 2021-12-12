n = int(input())
a = list(map(int, input().split()))
b = list(map(int, input().split()))

orth = 0
for i in range(n):
    orth += a[i]*b[i]
if orth == 0:
    print("Yes")
else:
    print("No")
