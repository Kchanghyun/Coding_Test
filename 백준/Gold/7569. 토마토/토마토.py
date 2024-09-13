import sys
from collections import deque

m, n, h = map(int, sys.stdin.readline().split())

matrix = [[list(map(int, sys.stdin.readline().split())) for _ in range(n)] for _ in range(h)]
visited = [[[False]*m for _ in range(n)] for _ in range(h)]

dx = [1, -1, 0, 0, 0, 0]
dy = [0, 0, 1, -1, 0, 0]
dz = [0, 0, 0, 0, 1, -1]

queue = deque()

def bfs():
    while(queue):
        x, y, z = queue.popleft()
        for i in range(6):
            nx = x + dx[i]
            ny = y + dy[i]
            nz = z + dz[i]

            if 0 <= nx < h and 0 <= ny < n and 0 <= nz < m and not visited[nx][ny][nz] and matrix[nx][ny][nz] == 0:
                visited[nx][ny][nz] = True
                matrix[nx][ny][nz] = matrix[x][y][z] + 1
                queue.append((nx, ny, nz))

answer = 0
for i in range(h):
    for j in range(n):
        for k in range(m):
            if matrix[i][j][k] == 1 and not visited[i][j][k]:
                queue.append((i, j, k))
                visited[i][j][k] = True
bfs()

for a in matrix:
    for b in a:
        for c in b:
            if c == 0:
                print(-1)
                exit(0)
        answer = max(answer, max(b))

print(answer-1)