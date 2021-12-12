from collections import Counter, deque, defaultdict

n = int(input())
s = []
for i in range(n):
  si = input()
  s.append(si)
c = Counter(s)
print(c.most_common()[0][0])