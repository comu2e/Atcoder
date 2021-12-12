from collections import Counter, deque, defaultdict

n = int(input())
martials = []
easy = [[] for i in range(n+1)]
for i in range(n):
    a = list(map(int, input().split()))
    if a[1] == i:
        easy[i].append([i, a[0]])
for i in range(n):
    marital
