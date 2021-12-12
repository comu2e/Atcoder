n = int(input())
l = []
A = []
for i in range(n):
    inp = list(map(int, input().split()))
    l.append(inp[0])
    a = tuple(inp[1:])
    A.append(a)
print(len(set(A)))
