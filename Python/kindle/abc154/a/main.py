s,t = list(map(str,input().split()))
a,b = list(map(int,input().split()))
u = input()
if s == u:
    print(a-1,b)
else:
    print(a,b-1)