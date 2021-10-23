n, k = map(int, input().split())
i = 0
cnt = 1
num = ""


def base10to(n, b):
    if (int(n/b)):
        return base10to(int(n/b), b) + str(n % b)
    return str(n % b)


def base10from(num, b):
    n = 0
    numlist = list(num)
    while (numlist):
        n *= b
        n += int(numlist.pop(0))
    return n


num = base10to(n, k)
print(len(str(num)))
