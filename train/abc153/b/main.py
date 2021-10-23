h, n = map(int, input().split())
A = list(map(int, input().split()))

sum = sum(A)
if sum >= h:
    print("Yes")
else:
    print("No")
