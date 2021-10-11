n,k = map(int,input().split())
c = list(map(int,input().split()))
color = {}
for i in range(n):
    color.setdefault(c[i],0)
tmp = 0

for i in range(k):
    if color[c[i]] == 0:
        tmp += 1
    color[c[i]] += 1
print(color)
ans = tmp

for i in range(n-k):
    if color[c[i]] == 1:
        tmp -= 1
    color[c[i]] -= 1
    if color[c[i+k]]  == 0:
        tmp += 1
    color[c[i+k]] += 1
    ans = max(ans,tmp)
print(ans)
        
    
        
    