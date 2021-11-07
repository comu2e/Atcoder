from itertools import accumulate, product, permutations, combinations
t = int(input())
for i in range(t):
    l, r = map(int, input().split())
    n = r-l*2
    if n < 0:
        print(0)
        return
    print((n+1)*(n+2)//2)
