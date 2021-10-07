n = int(input())
a = list(map(int,input().split()))

mul = 1
for i in a:
    mul *= i
if mul > 10**8:
    print(-1)
else:
    print(mul)