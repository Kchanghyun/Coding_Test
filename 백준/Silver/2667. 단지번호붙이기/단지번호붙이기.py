# dfs 재귀버전
import sys

input = sys.stdin.readline

N = int(input())
map = [list(map(int, input().strip())) for _ in range(N)]
visited = [[False] * N for _ in range(N)]

dx = [1, 0, -1, 0]
dy = [0, 1, 0, -1]

def dfs(y, x):
    global each
    each += 1
    for i in range(4):
        ny = y + dy[i]
        nx = x + dx[i]
        if 0 <= ny < N and 0 <= nx < N:
            if map[ny][nx] == 1 and not visited[ny][nx]:
                visited[ny][nx] = True
                dfs(ny, nx)

result = []
each = 0
for i in range(N):
    for j in range(N):
        if map[i][j] == 1 and not visited[i][j]:
            visited[i][j] = True
            each = 0
            dfs(i, j)
            result.append(each)


result.sort()
print(len(result))
for i in result:
    print(i)