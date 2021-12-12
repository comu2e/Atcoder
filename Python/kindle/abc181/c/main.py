from itertools import combinations
import math
n = int(input())
plane = []
for i in range(n):
    plane.append(list(map(int,input().split())))

isSame = False
for root in combinations(range(0,n),3):
    ax,ay = plane[root[0]]
    bx,by = plane[root[1]]
    cx,cy = plane[root[2]]
    
    if ((ax-bx)*(ay-cy) == (ax-cx)*(ay-by) ):
        isSame = True

if isSame:
    print("Yes")
else:
    print("No")