
n = int(input())

def divide(n):
    i = 1
    divisor = list()
    while i*i <= n:
        if n % i == 0:
            divisor.append(i)
            divisor.append(n//i)
        i += 1
    divisor =set(divisor)
    return divisor

ans = list(divide(n))
ans.sort()

for a in ans:
    print(a)