n = int(input())
s = list(map(int, input().split()))


def area(a, b):
    return 4*a*b + 3*a+3*b


T = set()
for a in range(1, 1001):
    for b in range(1, 1001):
        T.add(area(a, b))
ans = 0

for x in s:
    if x not in T:
        ans += 1
print(ans)
