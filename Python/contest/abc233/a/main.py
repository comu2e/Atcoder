import math
x,y = map(int,input().split())


for i in range(101):
    if 10*i + x < y:
        pass
    else:
        print(i)
        break

