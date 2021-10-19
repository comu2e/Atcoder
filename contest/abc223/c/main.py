import bisect
n = int(input())
dis = []
vec = []
sec = []
for i in range(n):
    a, b = list(map(int, input().split()))
    dis.append(a)
    vec.append(b)
    sec.append(a/b)
index = 0
left = 0
res_time = sum(sec)/2
i = 0
while res_time > 0:
    if dis[i]/vec[i] <= res_time:
        res_time -= dis[i]/vec[i]
        left += dis[i]
        i += 1
    else:
        left += float(vec[i]*res_time)
        break

print(left)
