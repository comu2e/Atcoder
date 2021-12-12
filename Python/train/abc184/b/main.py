n, x = map(int, input().split())
s = input()
for question in s:
    if x > 0:
        if question == "o":
            x += 1
        else:
            x -= 1
    else:
        if question == "o":
            x += 1
print(x)
