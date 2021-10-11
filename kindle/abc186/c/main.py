n = int(input())
a = list(map(int,input().split()))
sum = 0

for i in range(n):
    for j in range(j+1,n+1):
        sum += abs(a[i]-a[j])
print(sum)