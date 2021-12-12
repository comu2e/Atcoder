import math
n = int(input())
x = list(map(int,input().split()))

def manhattan(x):
    return sum(list(map(lambda el:abs(el),x)))
def yuchlid(x):
    return math.sqrt(sum(list(map(lambda el :abs(el)**2,x))))
def chebichef(x):
    return max(list(map(lambda el:abs(el),x)))
print(manhattan(x))
print(yuchlid(x))
print(chebichef(x))