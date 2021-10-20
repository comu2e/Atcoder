from itertools import accumulate, product, permutations, combinations

n, m = map(int, input().split())
a = list(map(int, input().split()))
sum_vote = sum(a)
limit = sum_vote/(4*m)
limit_a = []
for i in a:
    if limit <= i:
        limit_a.append(i)
if len(limit_a) >= m:
    print("Yes")
else:
    print("No")
