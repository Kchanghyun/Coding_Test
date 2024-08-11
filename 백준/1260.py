# import sys
# from collections import deque
#
# N, M, V = map(int, sys.stdin.readline().split())
#
# graph = [[False] * (N+1) for _ in range(N+1)]
#
# visited1 = [False] * (N+1)  # bfs 방문
# visited2 = [False] * (N+1)  # dfs 방문
#
# for i in range(M):
#     x, y = map(int, sys.stdin.readline().split())
#     graph[x][y] = True
#     graph[y][x] = True
#
# def bfs(v):
#     queue = deque([v])
#     visited1[v] = True
#     while queue:
#         x = queue.popleft()
#         print(x, end=' ')
#         for i in range(1, N+1):
#             if not visited1[i] and graph[x][i]:
#                 queue.append(i)
#                 visited1[i] = True
#
#
# def dfs(v):
#     visited2[v] = True
#     print(v, end=' ')
#     for i in range(1, N+1):
#         if not visited2[i] and graph[v][i]:
#             dfs(i)
#
#
# dfs(V)
# print()
# bfs(V)