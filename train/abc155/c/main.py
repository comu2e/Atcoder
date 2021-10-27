import collections
n = int(input())
dic = []
for i in range(n):
    dic.append(input())
c = collections.Counter(dic)
maxCount = max(c.items(), key=lambda x: x[1])[1]
maxWord = max(c.items(), key=lambda x: x[1])[0]
ans = []
for k, v in c.items():
    if v == maxCount:
        ans.append(k)
ans.sort()
for a in ans:
    print(a)
