
bingo = []
for i in range(3):
    bingo.append(list(map(int, input().split())))
M = []
for _ in range(3):
    row = []
    for _ in range(3):
        row.append(False)
    M.append(row)
n = int(input())
for i in range(n):
    b = int(input())
    for j in range(3):
        for k in range(3):
            if bingo[j][k] == b:
                M[j][k] = True

is_bingo = False
for i in range(3):
    if M[i][0] and M[i][1] and M[i][2]:
        is_bingo = True

for i in range(3):
    if M[0][i] and M[1][i] and M[2][i]:
        is_bingo = True

if M[0][0] and M[1][1] and M[2][2]:
    is_bingo = True

if M[0][2] and M[1][1] and M[2][0]:
    is_bingo = True

if is_bingo:
    print("Yes")
else:
    print("No")
