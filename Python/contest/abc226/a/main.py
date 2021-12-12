s = input()
idx = s.index(".")
num = int(s[idx+1])

if num < 5:
    ans = s[:idx]
    print(ans)
else:
    print(int(s[:idx])+1)
