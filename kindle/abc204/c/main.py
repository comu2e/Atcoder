from collections import deque

n,m = map(int,input().split())

cities = [[] for i in range(n+1)]

for i in range(m):
    a,b = list(map(int,input().split()))
    cities[a].append(b)

def bfs(city)->int:
    queue = deque()
    visited = [False] *(n+1)
    visited[city] = True
    queue.append(city)
    res = 1
    while queue:
        now_city = queue.popleft()

        for to_city in cities[now_city]:
            if visited[to_city] == False:
                visited[to_city] = True
                res += 1
                queue.append(to_city)
    return res

ans = 0
for i in range(1,n+1):
    ans += bfs(i)
print(ans)