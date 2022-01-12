n,x = map(int,input().split())
now = [1]

for i in range(n):
    lis = list(map(int,input().split()))
    next = []
    for j in range(1,lis[0] + 1):
        for k in range(len(now)):
            next.append(now[k] * lis[j])
    now = next

print(now.count(x))
