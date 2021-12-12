s = list(input())
t = list(input())

length = len(s)
lengthT = len(t)
ans = lengthT
for start in range(length-lengthT+1):
    diff = 0
    for i in range(lengthT):
        if t[i] != s[start+i]:
            diff += 1
    ans = min(ans, diff)
print(ans)
