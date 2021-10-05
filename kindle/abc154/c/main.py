n = int(input())
a = list(map(int,input().split()))
set_a = set(a)
if len(set_a) == n:
    print("YES")
else:
    print("NO")