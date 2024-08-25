import sys
from collections import deque

N, M = map(int, sys.stdin.readline().split())

graph = [[0] * (N+1) for _ in range(N+1)]

for i in range(M):
    x, y = map(int, sys.stdin.readline().split())
    graph[x][y] = 1
    graph[y][x] = 1

def bfs(v):
    queue = deque([v])
    visited[v] = True
    while queue:
        x = queue.popleft()
        for i in range(1, N+1):
            if not visited[i] and graph[x][i]:
                queue.append(i)
                visited[i] = True

cnt = 0
visited = [False] * (N+1)

for i in range(1, N+1):
    if not visited[i]:
        cnt += 1
        bfs(i)

print(cnt)