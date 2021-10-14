n = int(input())

ans = 0
points = []
for i in range(n):
    points.append(list(map(int, input().split())))


def slope(p1, p2):
    return (p1[1]-p2[1])/(p1[0]-p2[0])


for i in range(n):
    for j in range(i+1, n):
        s = slope(points[i], points[j])
        if -1 <= s <= 1:
            ans += 1
print(ans)
