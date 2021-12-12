n,k = list(map(int,input().split()))
r,s,p = list(map(int,input().split()))
t = input()

ans = 0
hand = []
for i in range(n):
    if t[i] == "r":
        if i < k :
            ans += p         
            hand.append("p")
        elif k<= i and hand[i-k] != "p":
            ans += p
            hand.append("p")
        else:
            hand.append("x")
    if t[i] == "s":
        if i < k :
            ans += r
            hand.append("r")
        elif k<= i and hand[i-k] != "r":
            ans += r
            hand.append("r")
        else:
            hand.append("x")
    if t[i] == "p":
        if i < k :
            ans += s
            hand.append("s")
        elif k<= i and hand[i-k] != "s":
            ans += s
            hand.append("s")
        else:
            hand.append("x")
print(ans)