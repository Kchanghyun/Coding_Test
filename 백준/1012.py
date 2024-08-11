import sys
from collections import deque


def bfs(x, y):
    queue = deque([(x, y)])
    farm[x][y] = 0  # 방문처리
    dx = [1, -1, 0, 0]
    dy = [0, 0, 1, -1]

    while queue:
        cx, cy = queue.popleft()

        for i in range(4):
            nx = cx + dx[i]
            ny = cy + dy[i]

            if nx < 0 or nx >= m or ny < 0 or ny >= n:
                continue
            if farm[nx][ny] == 1:
                farm[nx][ny] = 0
                queue.append((nx, ny))


t = int(sys.stdin.readline())
for i in range(t):
    n, m, k = map(int, sys.stdin.readline().split())
    # points = []
    farm = [[0] * n for _ in range(m)]  # arr = [[0] * cols for _ in range(rows)] row = 행, col = 열
    # n개의 m짜리 리스트를 생성하는 코드라고 생각.
    snake = 0
    for j in range(k):
        x, y = map(int, sys.stdin.readline().split())
        # points.append((b, a))
        farm[y][x] = 1
    for a in range(m):
        for b in range(n):
            if farm[a][b] == 1:
                bfs(a, b)
                snake += 1
    print(snake)
