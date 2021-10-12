s = input()
rotate = []

for st in s:
    if st == "9":
        rotate.append("6")
    else:
        rotate.append(st)
print("".join(rotate))