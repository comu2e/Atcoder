n,k = map(int,input().split())

friends  = []
for i in range(n):
    friends.append(list(map(int,input().split())))
friends.sort()

now_village = 0

now_village += k

for i in range(n):
    friend_village = friends[i][0]
    friend_money = friends[i][1]

    if friend_village<=now_village:
        now_village+= friend_money
    else:
        break
print(now_village)