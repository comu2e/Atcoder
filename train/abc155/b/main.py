n = int(input())
a = list(map(int, input().split()))
flag = []
for el in a:
    if el % 2 == 0:
        if el % 3 == 0 or el % 5 == 0:
            flag.append(True)
        else:
            flag.append(False)
if False not in flag:
    print("APPROVED")
else:
    print("DENIED")
