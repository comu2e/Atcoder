import math
from itertools import combinations
n = int(input())

points = []
for i in range(n):
    points.append(list(map(int, input().split())))

cnt = 0

for root in combinations(points, 3):
    p1, p2, p3 = root
    x1, y1 = p1
    x2, y2 = p2
    x3, y3 = p3
    if (x2-x1)*(y3-y1)-(x3-x1)*(y2-y1) != 0:
        cnt += 1
print(cnt)
