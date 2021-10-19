X = int(input())
total = 100
year = 0
while total < X:
    total = total * 101 // 100
    year += 1

print(year)
