a,b,x = map(int,input().split())
def price(n):
    return a*n + b*len(str(n))
left = 1
right = 10**20

if x < price(1):
    print(0)
    exit()
    
while 1<right-left:
    pivot = (right+left)//2
    ans = price(pivot)

    if ans <= x:
        left = pivot
    else:
        right = pivot
if 10**9<left:
    left = 10**9
print(left)