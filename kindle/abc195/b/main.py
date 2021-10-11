a,b,w = map(int,input().split())

minAns = 10*14
maxAns = -10**14

gw = 1000*w

for x in range(1,10**6 + 10):
    if a*x <= gw <= b*x:
        maxAns = max(x,maxAns)
        minAns = min(x,minAns)

if maxAns == -10**14:
    print("UNSATISFIABLE")
else:
    print(minAns,maxAns)
    