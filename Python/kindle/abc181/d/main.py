s = input()
sSet = set(list(s))
eight_list = [8*i for i in range(13,125)]

for i in eight_list:
    eight_str = set(list(str(i)))
    if sSet & eight_str:
        print(i)
