from collections import deque

s = input()
sortedList = []
maxS = ""
minS = ""

for i in range(len(s)):
    sortedList.append(s[i:]+s[:i])
sortedList.sort()
print(sortedList[0])
print(sortedList[-1])
