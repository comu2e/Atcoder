n, r = map(int, input().split())
if n < 10:
    rate = 100*(10-n)
    rate += r
else:
    rate = r
print(rate)
