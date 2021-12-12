n = int(input())

sum = 0
cnt = 0
for i in range(1,10**6+1):
    sum += i
    if sum >= n:
        cnt = i
        break
print(cnt)
    