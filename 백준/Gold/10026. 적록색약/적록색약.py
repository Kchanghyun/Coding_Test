import sys
from collections import deque

n = int(sys.stdin.readline())
led = []
color = [0] * 2

for i in range(n):
    led.append(list(sys.stdin.readline().strip()))


def bfs(x, y, color, count):
    if count == 1 and color == 'G':
        color = 'R'
    dx = [1, -1, 0, 0]
    dy = [0, 0, 1, -1]
    queue = deque()
    queue.append((x, y))
    visited[x][y] = True
    while queue:
        cx, cy = queue.popleft()
        for i in range(4):
            nx = cx + dx[i]
            ny = cy + dy[i]
            if 0 <= nx < n and 0 <= ny < n:
                if count == 1 and led[nx][ny] == 'G':
                    led[nx][ny] = 'R'
                if led[nx][ny] == color and not visited[nx][ny]:
                    visited[nx][ny] = True
                    queue.append((nx, ny))


for k in range(2):
    visited = [[False] * n for _ in range(n)]
    for i in range(n):
        for j in range(n):
            if visited[i][j] == False:
                bfs(i, j, led[i][j], k)
                color[k] += 1

print(*color, sep=' ')