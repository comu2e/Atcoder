a, b, c = map(int, input().split())

if c == 0:
    if 0 < a <= b:
        print("Aoki")
    elif a == 0 and 0 < b:
        print("Aoki")
    else:
        print("Takahashi")
else:
    if 0 < a <= b:
        print("Takahashi")
    elif a == 0 and 0 < b:
        print("Takahashi")
    else:
        print("Aoki")
