import math
import itertools
n = int(input())
points = []
for i in range(n):
    points.append(list(map(input().split())))


ans = -1

for v in itertools.combinations(points, 2):
    point1, point2 = v
    distance = math.dist(point1, point2)
    if ans < distance:
        ans = distance
print("{:.10f}".format(ans))
