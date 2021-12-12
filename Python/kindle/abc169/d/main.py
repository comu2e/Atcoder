n = int(input())

def prime_factorize(n):
    if n == 1:
        return [1]
    prime_list = []
    i = 2
    while i*i <= n:
        if n % i == 0:
            prime_list.append(i)
            n//=i
        else:
            i += 1
        if n != 1:
            prime_list.append(n)
    
        return prime_list

prime_n = set(prime_factorize(n))

ans = 0

for p in prime_n:
    for e  in range(1,10**10):
        if n%(p**e) == 0:
            ans += 1
            n //= p**e
        else:
            break
print(ans)