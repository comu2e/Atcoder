n,M = map(int,input().split())
hand = []
for i in range(2*n):
    hand.append(input())

rank = [[0,i] for i in range(2*n)]
def judge(a,b):
    if (a == "G" and b == "P") or (a == "C" and b == "G") or (a == "P" and b == "C"):
        return 1
    elif a == b:
        return -1
    else:
        return 0
for j in range(M):
    for i in range(n):
        player1 = rank[2*i][1]
        player2 = rank[2*i+1][1]
        result = judge(hand[player1][j],hand[player2][j])
        if result != -1:rank[2*i+result][0] -= 1
    rank.sort()
for _,i in rank:print(i+1)