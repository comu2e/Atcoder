n = int(input())
digit = len(str(n))
listN = list(map(int,list(str(n))))
modListN = list(map(lambda x : x%3 ,listN))

zeroCnt = modListN.count(0)
oneCnt = modListN.count(1) 
twoCnt = modListN.count(2)  

if zeroCnt == digit:
    print(0)
else:
    if oneCnt + twoCnt == digit:
        print(-1)
    
    else:
        if oneCnt % 3 == 0:
            if twoCnt % 3 == 1:
                print(1)
            elif twoCnt % 3 == 2:
                print(2)
            else:
                print(0)
        elif oneCnt %3 == 1:
            if twoCnt % 3 == 1:
                print(0)
            elif twoCnt % 3 == 2:
                print(1)
            else:
                print(1)
        else:
            if twoCnt % 3 == 1:
                print(1)
            elif twoCnt % 3 == 2:
                print(2)
            else:
                print(1)          