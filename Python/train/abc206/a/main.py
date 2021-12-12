import math
n = int(input())
tax = math.floor(n * 1.080)

if tax < 206:
    print("Yay!")
elif tax == 206:
    print("so-so") 
else:
    print(":(")