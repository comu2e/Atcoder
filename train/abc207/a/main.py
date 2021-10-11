
a,b,c = list(map(int,input().split()))

ans1 = a+b
ans2 = b+c
ans3 = a+c
maxAns = max(ans1,ans2,ans3)
print(maxAns)