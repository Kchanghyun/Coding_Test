import sys
from collections import deque

N, M = map(int, sys.stdin.readline().split())

graph = []

for i in range(N):
    graph.append(list(map(int, sys.stdin.readline().strip())))


def bfs(x, y):
    # 위, 아래, 오른쪽, 왼쪽
    dx = [0, 0, 1, -1]
    dy = [1, -1, 0, 0]

    queue = deque()
    queue.append((x, y))

    while queue:
        x, y = queue.popleft()
        for i in range(4):
            nx = x + dx[i]
            ny = y + dy[i]

            # 위치 벗어나면 안됨
            if nx < 0 or nx >= N or ny < 0 or ny >= M:
                continue
            # 벽이므로 진행 불가
            if graph[nx][ny] == 0:
                continue
            if graph[nx][ny] == 1:
                graph[nx][ny] = graph[x][y] + 1
                queue.append((nx, ny))

    return graph[N-1][M-1]

print(bfs(0,0))