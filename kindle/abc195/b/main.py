import math
if __name__=='__main__':
    min_ans= 10**15
    max_ans = -10**15
    res = []
    a,b,w = list(map(int,input().split()))
    w_g = 1000 * w
    for x in range(1,10**6+10):
        if a*x <= w_g <= b*x:
            min_ans = min(min_ans,x)
            max_ans = max(max_ans,x)

    if min_ans == 10**15:
        print("UNSATISFIABLE")
    else:
        print(min_ans,max_ans)