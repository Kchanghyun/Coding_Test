import sys
from collections import deque

m, n, h = map(int, sys.stdin.readline().split())
# n행 m열

box = []
for i in range(h):
    for j in range(m):
        box.append(list(map(int, sys.stdin.readline().split())))

# def bfs(x, y):
#     queue = deque()
#     queue.append((x, y))
#     visited = [[[False] * n for _ in range(m)] for _ in range(h)]
#     while queue:
        