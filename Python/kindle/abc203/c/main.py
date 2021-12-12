n,k = map(int,input().split())
friends = []

for i in range(1,n+1):
    a,b = list(map(int,input().split()))
    friends.append([a,b])
friends.sort()

position = k

for i in range(n):
    city = friends[i][0]
    charge = friends[i][1]
    if city <= position:
        position += charge
    else:
        break
print(position)