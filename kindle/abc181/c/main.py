import math,itertools

def is_linear(a,b,c):
    ab_vec = [a[0]-b[0],a[1]-b[1]]
    ac_vec = [a[0]-c[0],a[1]-c[1]]
    
    
    if (ab_vec[0]*ac_vec[1] == ab_vec[1]*ac_vec[0]):
        return True
    else:
        return False
    

n = int(input())

position = []

for i in range(n):
    position.append(list(map(int,input().split())))

for comb in list(itertools.combinations(position,3)):
    a,b,c = comb
    res = is_linear(a,b,c)
    if res:
        print("Yes")
        break

if not res:
    print("No")