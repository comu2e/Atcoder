n = int(input())
a = list(map(int,input().split()))

sum = 0
for el in a:
    if el <= 10:
        pass
    elif 10<el:
        sum += el-10
print(sum)