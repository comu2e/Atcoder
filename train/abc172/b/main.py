s = input()
t = input()

cnt = 0
for i in range(len(s)):
    if s[i] == t[i]:
        cnt += 1
    else:
        pass
print(len(s)-cnt)
