n = int(input())
dices = []
flags = []
isSame = False
for _ in range(n):
    d1, d2 = list(map(int, input().split()))
    if d1 == d2:
        flags.append(True)
    else:
        flags = []

    if flags == [True]*3:
        isSame = True
if isSame == True:
    print("Yes")
else:
    print("No")
