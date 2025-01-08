import sys
from collections import deque

n, m = map(int, sys.stdin.readline().split())

graph = []
for i in range(n):
    graph.append(list(map(int, sys.stdin.readline().split())))

visited = [[False] * m for _ in range(n)]


# n행 m열 리스트
def bfs(x, y):
    dx = [1, -1, 0, 0]
    dy = [0, 0, 1, -1]
    graph[x][y] = 0
    queue = deque()
    queue.append((x, y))
    visited[x][y] = True
    while queue:
        cx, cy = queue.popleft()
        for i in range(4):
            nx = cx + dx[i]
            ny = cy + dy[i]
            if 0 <= nx < n and 0 <= ny < m and graph[nx][ny] == 1 and not visited[nx][ny]:
                visited[nx][ny] = True
                queue.append((nx, ny))
                graph[nx][ny] = graph[cx][cy] + 1


for i in range(n):
    for j in range(m):
        if graph[i][j] == 2:
            bfs(i, j)

for row in graph:
    print(*row, sep=' ')
