import bisect
a,b,x = map(int,input().split())

def price(n):
    d = len(str(n))
    return a*n + b*d
if x < price(1):
    print(0)
    exit()
left = 1
right = 10*20
while 1<right-left:
    n = (left+right)//2
    if price(n) <= x:
        left = n
    else:
        right = n
        
if 10**9 < left:
    left = 10**9
print(left)
