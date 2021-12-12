res = []
list = ["H","2B","3B","HR"]
for i in range(4):
    s = input()
    if s in list:
        idx = list.index(s)
        list[idx] = True
if list.count(True) == 4:
    print("Yes")
else:
    print("No")