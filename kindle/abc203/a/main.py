a,b,c = map(int,input().split())

if a == b and a != c:
    print(c)
elif a == c and a!=b:
    print(b)
elif b == c and b!=a:
    print(a)
elif a == b == c:
    print(a)
else:
    print(0)