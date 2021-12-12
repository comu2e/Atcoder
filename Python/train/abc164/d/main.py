s = input()
for i in range(len(s)):
    for j in range(len(s)):
        integer = s[i:-1 - j]
        try:
            if int(integer) % 2019 == 0:
                print(integer)
        except ValueError:
            pass
