import math
x = int(input())
assum = pow(10,3)
for a in range(-assum,assum):
    for b in range(-assum,assum):
        if pow(a,5) - pow(b,5) == x:
            print(a,b)
            exit()