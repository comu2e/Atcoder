x, y = map(int, input().split())

x, y = min(x, y), max(x, y)

if x + 3 <= y:
    print("No")
else:
    print("Yes")
