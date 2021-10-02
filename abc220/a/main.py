k = int(input())
a,b = map(int,input().split())

def Base_n_to_10(X,n):
    out = 0
    for i in range(1,len(str(X))+1):
        out += int(X[-i])*(n**(i-1))
    return out 

base_10_a = Base_n_to_10(a,k)
base_10_b = Base_n_to_10(b,k)
print(base_10_a*base_10_b)