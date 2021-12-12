s = input()
t = input()


alp = "abcdefghijklmnopqrstuvwxyz"
isFlag = False

for a in alp:
    if s+a == t:
        isFlag = True
        break
    
if isFlag:
    print("Yes")
else:
    print("No")
