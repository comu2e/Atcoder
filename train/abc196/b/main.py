import math
x = input()


try:
    point_idx = x.index(".")
    print(x[:point_idx])
except ValueError:
    print(x)