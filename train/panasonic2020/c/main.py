import math
a, b, c = map(int, input().split())
left = 4*a*b
right = (c-a-b)**2
if left < right and 0 < (c-a-b):
    print("Yes")
else:
    print("No")
