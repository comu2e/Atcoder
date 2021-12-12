a, b, k = map(int, input().split())

eat = min(a, k)
a -= eat
k -= eat

eat = min(b, k)

b -= eat
k -= eat
print(a, b)
