import math
p = int(input())
factYen = []
for i in range(1, 50):
    if math.factorial(i) <= p:
        factYen.append(math.factorial(i))
factYen.sort(reverse=True)
ans = 0
for yen in factYen:
    if p <= 0:
        break
    else:
        factCnt = p//yen
        p -= factCnt * yen
        ans += factCnt
print(ans)
