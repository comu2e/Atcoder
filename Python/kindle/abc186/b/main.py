h,m = map(int,input().split())
grid = []
for i in range(h):
    for j in  list(map(int,input().split())):
        grid.append(j)

sum = 0

for a in grid:
    sum += a - min(grid)
print(sum)