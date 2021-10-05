n,k = list(map(int,input().split()))
p = list(map(int,input().split()))

p_ex = []
for i in range(n):
    p_ex.append(( p[i]+ 1 )/2)

p_ex_cum = [p_ex[0]]

for i in range(1,n):
    p_ex_cum.append(p_ex_cum[i-1]+p_ex[i])

ans = -10**15
for i in range(n-k+1):
    if i == 0:
        ans_temp = p_ex_cum[i+k-1]
    else:
        ans_temp = p_ex_cum[i+k-1] - p_ex_cum[i-1]
    ans = max(ans,ans_temp)
print("{:.12f}".format(ans))