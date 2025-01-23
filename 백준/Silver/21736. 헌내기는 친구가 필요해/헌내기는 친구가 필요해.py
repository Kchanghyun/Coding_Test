import sys
from collections import deque

n, m = map(int, sys.stdin.readline().split())

# I 시작, P 사람, X 벽, O 빈 공간
# 또 bfs?

# 만날 수 있는 사람의 수 출력, 못 만나면 TT 출력
campus = []
visited = [[False] * m for _ in range(n)]
for i in range(n):
    campus.append(list(sys.stdin.readline().strip()))


def bfs(a, b, friends):
    dx = [1, -1, 0, 0]
    dy = [0, 0, 1, -1]

    visited[a][b] = True
    node = deque()
    node.append((a, b))
    while node:
        x, y = node.popleft()
        for i in range(4):
            nx = x + dx[i]
            ny = y + dy[i]

            if 0 <= nx < n and 0 <= ny < m:
                if not visited[nx][ny] and (campus[nx][ny] == 'O' or campus[nx][ny] == 'P'):
                    if campus[nx][ny] == 'P':
                        friends += 1
                    visited[nx][ny] = True
                    node.append((nx, ny))
    if friends == 0:
        return -1
    else:
        return friends

for i in range(n):
    for j in range(m):
        if campus[i][j] == 'I':
            cnt = bfs(i, j, 0)

if cnt == -1:
    print('TT')
else:
    print(cnt)