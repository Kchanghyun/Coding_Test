import sys

n, m = map(int,sys.stdin.readline().split())

board = [list(map(int, sys.stdin.readline().split())) for _ in range(n)]
visited = [[False] * m for _ in range(n)]

maxvalue = 0
move = [(0, 1), (0, -1), (1, 0), (-1, 0)]


def dfs(i, j, dsum, cnt):
    global maxvalue

    if cnt == 4:
        maxvalue = max(maxvalue, dsum)
        return

    for k in range(4):
        ni = i + move[k][0]
        nj = j + move[k][1]

        if 0 <= ni < n and 0 <= nj < m and not visited[ni][nj]:
            visited[ni][nj] = True
            dfs(ni, nj, dsum + board[ni][nj], cnt+1)
            visited[ni][nj] = False


def exce(i, j):
    global maxvalue
    for k in range(4):
        tmp = board[i][j]
        for l in range(3):
            t = (k+l)%4
            ni = i + move[t][0]
            nj = j + move[t][1]

            if not (0 <= ni < n and 0 <= nj < m):
                tmp = 0
                break
            tmp += board[ni][nj]
        maxvalue = max(maxvalue, tmp)


for a in range(n):
    for b in range(m):
        visited[a][b] = True
        dfs(a, b, board[a][b], 1)
        visited[a][b] = False
        exce(a, b)

print(maxvalue)