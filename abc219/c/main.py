from functools import reduce
from typing import *

x = input()
n = int(input())
sList = []
dic = "abcdefghijklmnopqrstuvwxyz" 

newDic = {}

for d in dic:
    cnt = 1
    for el in x:
        newDic[el] = cnt
        cnt += 1
for _ in range(n):
    sList.append(input())

resDic = {}
for s in sList:
    tempS = ""
    for i,v in enumerate(newDic):
        
        for el in s:
            if el == v:
                tempS += str(i)
        resDic[s] = int(tempS)

res = sorted(resDic.values())
print(res)