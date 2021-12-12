a, b, c, d = map(int, input().split())

turn_takahashi = True
while True:
    if turn_takahashi == True:
        c -= b
        turn_takahashi = False
    else:
        a -= d
        turn_takahashi = True
    if a <= 0 or c <= 0:
        break
if a > 0 and c <= 0:
    print("Yes")
else:
    print("No")
