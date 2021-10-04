s = input()
t = input()
listS = list(s)
listT = list(t)

length = len(listS)
isIn = False
if listS == listT:
    isIn = True
else:
    for i in range(len(s)-1):
        temp = list(s)
        temp[i],temp[i+1] = temp[i+1],temp[i]
        if temp == listT:
            isIn = True
            break

if isIn:
    print("Yes")
else:
    print("No")
