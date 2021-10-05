n = int(input())
h = [0]+list(map(int,input().split()))

dp = [10**15]*(n+1)
dp[1] = 0
dp[2] = abs(h[2]-h[1])
for i in range(3,n+1):
    minCost = min(dp[i-1]+abs(h[i] - h[i-1]),dp[i-2]+abs(h[i]-h[i-2]))
    dp[i] = minCost
print(dp[n])