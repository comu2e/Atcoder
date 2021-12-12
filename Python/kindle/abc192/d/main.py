import math
x = input()
m = int(input())
if len(x) == 1:
    if int(x) <= m:
        print(1)
    else:
        print(0)
    exit()
d = int(max(list((x))))
numx = int(x)

def int_base(s : str, base : int ):
    r = 0
    for c in s:
        r = r*base+int(c)
    return r
def check(n):
    return int_base(x, n) > m


left = d+1
right = m+2
pivot = (left + right) //2 

while right > left:
    pivot = (right + left) //2
    if check(pivot):
        right = pivot
    else:
        if left == pivot:
            break
        left = pivot

r = right
r = r - (d+1)
print(r)