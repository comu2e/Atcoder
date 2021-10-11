import math
x = int(input())
# 3
if x % 100 == 0:
    print(100)
else:
    print(math.ceil(x/100)*100 - x)