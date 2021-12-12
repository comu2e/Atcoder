import string
n = int(input())
s = input()
alp = string.ascii_letters
alp_push = alp[n:] + alp[:n]
print(alp_push)
ans = []
for st in s:
    canPush = True
    for ka,va in enumerate(alp):
        if va == st:
            for k,v in enumerate(alp_push):
                if va == st and canPush:
                    ans.append(v.upper())
                    canPush = False

print("".join(ans))