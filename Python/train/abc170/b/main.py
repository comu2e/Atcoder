x, y = map(int, input().split())
ans = 0
for i in range(0, x+1):
    for j in range(0, x+1):
        legs = 2*i + 4*j
        if i+j == x and legs == y:
            ans += 1
if ans > 0:
    print("Yes")
else:
    print("No")
