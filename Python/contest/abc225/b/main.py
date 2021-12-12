import collections
n = int(input())

tree = []
for i in range(n-1):
    A = list(map(int, input().split()))
    tree.append(A[0])
    tree.append(A[1])

c = collections.Counter(tree)
for k, v in c.items():
    if v == n-1:
        print("Yes")
        exit()
print("No")
