
n = int(input())
A = list(map(int,input().split()))
A.sort()
a = [i for i in range(1,n+1)]
if a == A:
    print("Yes")
else:
    print("No")