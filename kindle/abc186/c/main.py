N = int(input())

def judge_7_in_10(n):
    n = str(n)
    
    if "7" in n:
        return True
    else:
        return False

def judge_7_in_oct(n):
    flag = False
    oct = ""
    init_n = n
    while init_n > 0:
        oct += str(init_n % 8)
        init_n = init_n // 8
        if "7" in oct:
            flag = True
            return flag
            break
    return flag

cnt = 0            
for i in range(1,N+1):
    if not judge_7_in_10(i) and not judge_7_in_oct(i):
        cnt += 1
        
print(cnt)