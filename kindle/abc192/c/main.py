n,k = map(int,input().split())

def g(x,is_1):
    list_x = list(str(x))
    return int("".join(sorted(list_x,reverse=is_1)))

def f(x):
    return g(x,True) - g(x,False)

fi = n
for i in range(k):
    
    fi = f(fi)
print(fi)