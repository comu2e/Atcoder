n = int(input())
a = list(map(int,input().split()))
x = int(input())

sumA = 0
for i in a:
    sumA += i
modX = x // sumA

res = modX*n
sumA = modX*sumA
for j in a:
    if sumA > x:
       break

    sumA += j
    res += 1

print(res)