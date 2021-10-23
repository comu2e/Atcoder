n, k = map(int, input().split())
d = []
A = []
sunuke = [False]*n
for _ in range(k):
    d = int(input())
    A = list(map(int, input().split()))
    for el in A:
        sunuke[el-1] = True
print(sunuke.count(False))
