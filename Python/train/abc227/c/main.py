import math

n = int(input())


def log_abc(a, b, c):
    return math.log(a, 10) + math.log(b, 10) + math.log(c, 10)


cnt = 0
limit = 3*10**3
for a in range(10):
    for b in range(10):
        for c in range(10):
            if log_abc(a, b, c) == n:
                cnt += 1
print(cnt)
