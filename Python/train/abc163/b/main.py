n, m = map(int, input().split())
a = list(map(int, input().split()))
homework = sum(a)
if n < homework:
    print(-1)
else:
    print(n-homework)
