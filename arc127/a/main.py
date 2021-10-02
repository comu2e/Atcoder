N = int(input())


def countN(N):
    count = 0
    for i in range(len(N)):
        if N[i] == "1":
            count += 1
        else:
            break
    return count
res  = 0 
for i in range(N):
    counter = countN(str(i+1))
    res += counter
print(res)
