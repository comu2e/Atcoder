from bisect import bisect_left, bisect_right, bisect, insort_left, insort_right, insort

n,q = map(int,input().split())
A = list(map(int,input().split()))
A.sort()
for i in range(q):
  xi = int(input())
  right = bisect_right(A,xi) -1
  if A[right] == xi:
    print(n-right)
  else:
    print(n-right-1)