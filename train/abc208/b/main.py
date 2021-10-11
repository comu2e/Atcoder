import math
p = int(input())

fact_yen = list(map(lambda yen:math.factorial(yen),[i+1 for i in range(0,10)]))
fact_yen.sort(reverse=True)
print(fact_yen)
cnt = 0
for fact in fact_yen:
    residue = p % fact