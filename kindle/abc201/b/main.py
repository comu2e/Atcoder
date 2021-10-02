import math
n = int(input())
arr = {}
sorted_arr = {}
temp = -math.inf

for i in range(n):
    s,t = input().split()
    arr[s] = int(t)
    
sorted_arr = sorted(arr.items(),key=lambda x:x[1])
print(sorted_arr[-2][0])