n, a, b = map(int, input().split())
b_cnt = 0

if a != 0:
    if b != 0:
        b_cnt += n//(a+b) * a
        n -= n//(a+b) * (a+b)
        b_cnt += min(a, n % (a+b))
        print(b_cnt)
    else:
        print(n)
else:
    print(0)
