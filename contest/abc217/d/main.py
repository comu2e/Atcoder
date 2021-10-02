import bisect
import array
l,q=map(int,input().split())
a=array.array('i',[0,l])
# a = ["i" for i in range(l)]

for _ in range(q):
    c,x=map(int,input().split())
    y = bisect.bisect(a,x)
    if c==1:
        a.insert(y,x)
    else:
        print(a[y]-a[y-1])