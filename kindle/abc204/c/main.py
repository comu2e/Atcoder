from collections import deque
que=deque()

n,m = list(map(int,input().split()))
connect = [[] for i in range(n+1)]

for i in range(m):
    a,b = list(map(int,input().split()))
    connect[a].append(b)

def bfs(start:int)->int:
    visited = [False]*(n+1)
    visited[start] = True
    cnt = 1
    que = deque()
    que.append(start)
    while que:
        now_city = que.popleft()
        for to_city in connect[now_city]:
            if visited[to_city] == False:
                visited[to_city] = True
                cnt += 1
                que.append(to_city)
    return cnt

ans = 0
for i in range(1,n+1):
    ans += bfs(i)
print(ans)
    