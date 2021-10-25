import string
n = int(input())
s = input()
alpha = list(string.ascii_uppercase)
ans = ""
for e in list(s):
    idx = alpha.index(e)
    idx += n
    idx %= 26
    ans += alpha[idx]
print(ans)
