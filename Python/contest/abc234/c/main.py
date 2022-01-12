K = int(input())

digit = 0
min_k = 0
for i in range(1000):
    min_k = 2**i-1
    if min_k < K:
        pass
    else:
        break
print(min_k)
