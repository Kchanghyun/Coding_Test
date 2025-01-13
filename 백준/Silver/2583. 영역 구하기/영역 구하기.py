import sys
from collections import deque

m, n, k = map(int, sys.stdin.readline().split())

board = [[0] * n for _ in range(m)]
visited = [[False] * n for _ in range(m)]
ret = []

for i in range(k):
    x1, y1, x2, y2 = map(int, sys.stdin.readline().split())
    for j in range(y1, y2):
        for l in range(x1, x2):
            board[m-1-j][l] = 1

def bfs(a, b, board, ret):
    deq = deque()
    deq.append((a,b))
    visited[b][a] = True
    width = 1
    dx = [1, -1, 0, 0]
    dy = [0, 0, 1, -1]

    while deq:
        x, y = deq.popleft()
        for i in range(4):
            nx = x + dx[i]
            ny = y + dy[i]

            if 0 <= nx < n and 0 <= ny < m:
                if board[ny][nx] == 0 and not visited[ny][nx]:
                    deq.append((nx, ny))
                    visited[ny][nx] = True
                    width += 1
    ret.append(width)


for i in range(m):
    for j in range(n):
        if board[i][j] == 0 and not visited[i][j]:
            bfs(j, i, board, ret)

print(len(ret))
print(*sorted(ret), sep=' ')