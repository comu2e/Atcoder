import math
a, b = map(int, input().split())

price = []
for i in range(1, 10000):
    price8 = math.floor(0.08 * i)
    price10 = math.floor(0.10*i)
    if price8 == a and price10 == b:
        price.append(i)
if len(price) != 0:
    min_price = min(price)
    print(min_price)
else:
    print(-1)
