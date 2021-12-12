n = input()

if len(n) < 4:
    print((4-len(n))*"0" + n)
else:
    print(n)
    