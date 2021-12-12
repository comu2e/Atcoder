s = input()
s = list(s)
flag = []
for i,v in enumerate(s):
    if v == v.lower() and i%2 == 0:
        flag.append(True)
    elif v == v.upper() and i%2 ==0:
        flag.append(False)
    
    if v == v.upper() and i%2 == 1:
        flag.append(True)
    elif v == v.lower() and i%2 ==1:
        flag.append(False)

if not False in flag:
    print("Yes")
else:
    print("No")