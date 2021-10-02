n = int(input())
arr = []
i = 1
while i**2 <= n:
    if n%i == 0:
        arr.append(i)
        if i != n//i:
            arr.append(n//i)
    i += 1
arr.sort()
for j in arr:
    print(j)
     