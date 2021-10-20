from collections import Counter
n = int(input())
a = list(map(int, input().split()))
members = [0] * n
set_members = set(a)
count_members = Counter(a)

for i in list(set_members):
    member = count_members[i]
    members[i-1] = member

for m in members:
    print(m)
