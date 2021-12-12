import string
p = list(map(int,input().split()))
alp = list(string.ascii_lowercase)
conv = []
for i in p:
    conv.append(alp[i-1])
print("".join(conv))