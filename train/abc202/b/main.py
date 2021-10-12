s = input()
rotate = []

for st in s:
    if st == "9":
        rotate.append("6")
    elif st == "6":
        rotate.append("9")
    else:
        rotate.append(st)
rotate.reverse()
print("".join(rotate))