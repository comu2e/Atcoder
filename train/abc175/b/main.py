n = int(input())
points = list(map(int, input().split()))
cnt = 0
for i in range(n):
    for j in range(i, n):
        for k in range(j, n):
            a = points[i]
            b = points[j]
            c = points[k]
            if abs(a-b) < c < a+b and a != b and a != c and b != c:
                cnt += 1
print(cnt)
