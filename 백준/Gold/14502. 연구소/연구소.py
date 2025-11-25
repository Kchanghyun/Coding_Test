import sys
import copy
from itertools import combinations
from collections import deque

input = sys.stdin.readline

"""
N x M 직사각형
연구소는 빈칸, 벽으로 이루어져 있음. 벽은 칸 하나를 가득 차지한다.
일부 칸은 바이러스 존재, 상하좌우로 인접한 빈 칸으로 퍼져나갈 수 있음.
새로 세울 수 있는 벽의 개수 3개. 꼭 3개 세워야 함.
0은 빈칸, 1은 벽, 2는 바이러스
벽 3개 세운 다음 2를 찾아서 bfs로 1나오기 전까지 2로 채운 다음 0의 개수 세면 될 거 같은데
벽 3개를 어떻게 세우지
"""

N, M = map(int, input().split())
graph = [list(map(int, input().split())) for _ in range(N)]
empty = []


def bfs(maps):
    q = deque()
    dx = [0, 1, 0, -1]
    dy = [1, 0, -1, 0]
    for i in range(N):
        for j in range(M):
            if maps[i][j] == 2:
                q.append((i, j))
    while q:
        x, y = q.popleft()
        for i in range(4):
            nx = x + dx[i]
            ny = y + dy[i]
            if 0 <= nx < N and 0 <= ny < M:
                if maps[nx][ny] == 0:
                    maps[nx][ny] = 2
                    q.append((nx, ny))
    return sum(row.count(0) for row in maps)


# graph에서 0의 좌표 구하기
for i in range(N):
    for j in range(M):
        if graph[i][j] == 0:
            empty.append((i,j))

answer = 0
# 그 중에서 3개 조합해서 temp로 graph를 복사하고 temp를 조작해서 벽 세워보기
# 벽 세워보고 bfs 돌려서 0의 개수 return 받아서 max 값 비교하기
for walls in combinations(empty, 3):
    temp = copy.deepcopy(graph)

    for x, y in walls:
        temp[x][y] = 1

    safe = bfs(temp)
    answer = max(answer, safe)

print(answer)
