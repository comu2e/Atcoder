n = int(input())
a = list(map(int, input().split()))

includeZero = 0 in a
if includeZero:
    print(0)
else:
    mul = 1
    for i in a:
        mul *= i
        if mul > 10**18:
            print(-1)
            exit()
        else:
            pass
    print(mul)
