import sys
from collections import deque

N = int(sys.stdin.readline())

graph = []
visited = [[False] * (N) for _ in range(N)]
home_count = []  # 단지에 속하는 집의 수

for i in range(N):
    home_num = list(map(int, sys.stdin.readline().strip()))

    for j in range(N):
        if home_num[j] == 1:
            graph.append((i, j))


def bfs():
    dx = [1, -1, 0, 0]
    dy = [0, 0, 1, -1]
    count = 0
    # for i in range(1, N + 1):
    #     for j in range(1, N + 1):
    while graph:
        x, y = graph.pop(0)
        if not visited[x][y]:
            count += 1
            queue = deque()
            queue.append((x, y))
            visited[x][y] = True
            home = 1
            while queue:
                x, y = queue.popleft()
                for i in range(4):
                    nx = x + dx[i]
                    ny = y + dy[i]
                    if nx < 0 or nx >= N or ny < 0 or ny >= N and (nx, ny) not in graph:
                        continue
                    if (nx, ny) in graph and not visited[nx][ny]:
                        # print('nx, ny = {}, {}'.format(nx, ny))
                        queue.append((nx, ny))
                        visited[nx][ny] = True
                        home += 1
            home_count.append(home)

    return count


print(bfs())
home_count.sort()
print(*home_count, sep="\n")
#
# import sys
# from collections import deque
#
# N = int(sys.stdin.readline().strip())
#
# graph = set()  # 집합으로 변경
# visited = [[False] * N for _ in range(N)]  # N x N 크기로 변경
# home_count = []  # 단지에 속하는 집의 수
#
# for i in range(N):
#     home_num = list(map(int, sys.stdin.readline().strip()))
#     for j in range(N):
#         if home_num[j] == 1:
#             graph.add((i, j))  # 집합에 추가
#
#
# def bfs(start_x, start_y):
#     dx = [1, -1, 0, 0]
#     dy = [0, 0, 1, -1]
#     count = 0
#     queue = deque([(start_x, start_y)])
#     visited[start_x][start_y] = True
#     home = 0
#
#     while queue:
#         x, y = queue.popleft()
#         home += 1  # 현재 집을 카운트
#
#         for i in range(4):
#             nx, ny = x + dx[i], y + dy[i]
#             if 0 <= nx < N and 0 <= ny < N and not visited[nx][ny] and (nx, ny) in graph:
#                 visited[nx][ny] = True
#                 queue.append((nx, ny))
#
#     return home
#
#
# def count_houses():
#     total_count = 0
#     for x, y in graph:
#         if not visited[x][y]:
#             home_count.append(bfs(x, y))
#             total_count += 1
#     return total_count
#
#
# print(count_houses())
# print(sorted(home_count))
