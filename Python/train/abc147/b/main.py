s = input()
cnt = 0
temp = list(s)
cnt = 0
if len(temp) % 2 == 0:
    length = len(temp) // 2
else:
    length = int(len(temp) / 2)
for i in range(length):
    if temp[i] != temp[-i-1]:
        cnt += 1
print(cnt)
