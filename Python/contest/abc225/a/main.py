import itertools

n = input()

ans = set()
all = itertools.permutations(n, len(n))
for x in all:
    ans.add(x)
print(len(ans))
