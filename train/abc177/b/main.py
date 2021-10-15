s = input()
t = input()

min = len(t)

for i in range(len(s)-len(t)):
    s_str = s[i:i+len(t)]
    for idx in range(len(t)):
        if s_str[idx] == t[idx]:
