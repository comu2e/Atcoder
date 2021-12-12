n, x = map(int, input().split())
a = list(map(int, input().split()))

a_prime = []

for i in range(n):
    if a[i] == x:
        pass
    else:
        a_prime.append(a[i])
print(*a_prime)
