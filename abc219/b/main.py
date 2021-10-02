s1 = input()
s2 = input()
s3 = input()
t = input()

res = ""
for i in t:
    if i == "1":
        res += s1
    if i == "2":
        res += s2
    if i == "3":
        res += s3

print(res)