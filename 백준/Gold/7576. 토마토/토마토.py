import sys
from collections import deque

M, N = map(int, sys.stdin.readline().split())

dx = [1, -1, 0, 0]
dy = [0, 0, 1, -1]

tray = []
for i in range(N):
    tray.append(list(map(int, sys.stdin.readline().split())))

queue = deque()

for i in range(N):
    for j in range(M):
        if tray[i][j] == 1:
            queue.append((i, j))

while queue:
    x, y = queue.popleft()
    for i in range(4):
        nx = x + dx[i]
        ny = y + dy[i]

        if 0 <= nx < N and 0 <= ny < M and tray[nx][ny] == 0:
            tray[nx][ny] = tray[x][y] + 1
            queue.append((nx, ny))

day = 0

for row in tray:
    for tomato in row:
        if tomato == 0:
            print(-1)
            exit(0)
    day = max(day, max(row))

print(day-1)