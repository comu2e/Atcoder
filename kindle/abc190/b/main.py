n,s,d = map(int,input().split())

is_defeat = False
for i in range(n):
    x,y = map(int,input().split())
    if x < s and d < y:
        print("Yes")
        is_defeat = True
        break


if not is_defeat:
    print("No")