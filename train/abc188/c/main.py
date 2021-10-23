
n = int(input())
a = list(map(int, input().split()))

match = a
for j in range(2**n-1):
    for i in range(j):
        win = match
        match = []
        if win[2*i] > win[2*i+1]:
            match.append(win[2*i])
        else:
            match.append(win[2*i+1])

    print(match)
