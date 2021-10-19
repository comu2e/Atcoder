a, b = map(int, input().split())
flag = False
for i in range(a, b+1):
    if i % k == 0:
        flag = True
        break
if flag == True:
    print("OK")
else:
    print("NG")
