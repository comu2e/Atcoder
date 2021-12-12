n = int(input())
cnt = 0
able_set = set()
for a in range(2, 100 + pow(10,5)):
    for b in range(2,100):
        if pow(a,b) <= n:
            able_set.add(pow(a,b))

print(n-len(ab))