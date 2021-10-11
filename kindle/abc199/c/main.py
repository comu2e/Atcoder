n = int(input())
s = [0] + list(input())
q = int(input())
isReverse = False

temp = s
for i in range(q):
    query = list(map(int,input().split()))
    t = query[0]
    if t == 1:
        a,b = query[1:]
        if not isReverse:
            s[a],s[b] = s[b],s[a]
        else:
            if a <= n:
                a += n
            else:
                a -= n
            if b <= n:
                b += n
            else:
                b -= n
            s[a],s[b] = s[b],s[a]    
    else:
        if isReverse:
            isReverse = False
            tmep = s
        else:
            isReverse = True
        
if not isReverse:
    s = s[1:n+1]  + s[n+1:] 
else:
    s = s[n+1:] + s[1:n+1]
print("".join(s))
        