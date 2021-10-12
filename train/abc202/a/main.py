dice = list(map(int,input().split()))
num = [i for i in range(1,7)]

print(sum(num)-sum(dice))