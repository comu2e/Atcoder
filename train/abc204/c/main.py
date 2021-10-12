from collections import deque

n,m = map(int,input().split())
connect = []
for i in range(m):
    connect.append(list(map(int,input().split())))


def bfs(start):
    que = deque()
    visited = [False] * (n+1)
    visited[start] = True
    que.add(start)
    while que:
        now = que.popleft()
        for to in connect:
            if visited[to[1]] == False:
                visited[to[1]]