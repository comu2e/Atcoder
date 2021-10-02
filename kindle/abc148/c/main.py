import math

def lcm(x,y):
    return (x*y)/math.gcd(x,y)

a,b = map(int,input().split())

print(int(lcm(a,b)))