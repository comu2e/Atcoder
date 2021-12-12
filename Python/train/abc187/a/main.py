a, b = input().split()

aSum = sum(list(map(int, list(a))))
bSum = sum(list(map(int, list(b))))
max = max(aSum, bSum)
print(max)
