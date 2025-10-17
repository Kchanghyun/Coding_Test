import sys
from collections import deque

n, m = map(int, sys.stdin.readline().split())
visited = [[False] * m for _ in range(n)]
painting = [list(map(int, sys.stdin.readline().split())) for _ in range(n)]
# for _ in range(n):
#     painting.append(list(map(int, sys.stdin.readline().split())))

dy = [0, 1, 0, -1]
dx = [1, 0, -1, 0]


def bfs(y, x):
    rs = 1
    node = deque([(y, x)])
    while node:
        ey, ex = node.popleft()
        for k in range(4):
            ny = ey + dy[k]
            nx = ex + dx[k]
            if 0 <= ny < n and 0 <= nx < m:
                if painting[ny][nx] == 1 and not visited[ny][nx]:
                    rs += 1
                    visited[ny][nx] = True
                    node.append((ny, nx))
    return rs


cnt = 0
maxv = 0

for i in range(0, n):
    for j in range(0, m):
        if painting[i][j] == 1 and not visited[i][j]:
            visited[i][j] = True
            # 전체 그림 개수 +1
            cnt += 1
            # BFS > 그림 크기 구하기
            maxv = max(maxv, bfs(i, j))

print(cnt)
print(maxv)
