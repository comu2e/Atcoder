s = input().split()
ans = []

for word in s:
    if word == "Left":
        ans.append("<")
    elif word == "Right":
        ans.append(">")
    else:
        ans.append("A")
print(*ans)
