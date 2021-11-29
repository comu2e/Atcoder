n, k, a = map(int, input().split())
rank = [i+1 for i in range(a-1, n)]
for i in range(a-1):
    rank.append(i+1)
print(rank[k % n - 1])
