n = int(input())
a = list(map(int,input().split()))

mul = 1
for i in a:
    mul *= i     
    if mul > 10**18:
        print(-1)
        mul = -1
        
        break
        

if mul != -1:
    print(mul)