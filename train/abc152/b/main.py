a, b = map(int, input().split())

A = str(a)*b
B = a*str(b)

ans = [A, B]
ans.sort()
print(ans[0])
