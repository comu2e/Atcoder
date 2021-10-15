import math
n, d = map(int, input().split())
points = []
for i in range(n):
    points.append(list(map(int, input().split())))


def distance(point):
    return point[0]**2 + point[1] ** 2


cnt = 0
for point in points:
    if distance(point) <= d**2:
        cnt += 1
print(cnt)
