x,k,d = list(map(int,input().split()))
x = abs(x)
if 0< x-k*d:
    print(abs(x-k*d))
else:
    move_cnt = k -x//d
    jumb_before = x- d*(x//d)
    jumb_after = jumb_before-d
    if move_cnt%2 == 0:
        print(abs(jumb_before))
    else:
        print(abs(jumb_after))
        
    