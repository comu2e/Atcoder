n,x = map(int,input().split())
a = list(map(int,input().split()))
dis_a = []
for i,p in enumerate(a):
    if i%2 == 1:
        dis_a.append(p-1)
    else:
        dis_a.append(p)

sum_p = sum(dis_a)
if sum_p <= x:
    print("Yes")
else:
    print("No")