n = int(input())
s = input()

for idx,ch in enumerate(s):
    if ch == "1":
        if idx % 2 == 0:
            print("Takahashi")
        else:
            print("Aoki")
        break