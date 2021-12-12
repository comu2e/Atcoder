s = input()
cnt = 0
if s == "RRR":
    cnt = 3
elif s == "RRS" or s == "SRR":
    cnt = 2
elif s == "RSS" or s == "SRS" or s == "SSR" or s == "RSR":
    cnt = 1
else:
    cnt = 0
print(cnt)
