import sys
from collections import deque

n = int(sys.stdin.readline())

a = [list(map(int, sys.stdin.readline().split())) for _ in range(n)]

# 단방향을 가진 그래프
graph = {i: [] for i in range(n)}
for i in range(n):
    for j in range(n):
        if a[i][j] == 1:
            if j not in graph[i]:
                graph[i] += [j]

def bfs(node):
    tmp = []
    queue = deque([node])
    visited = [False] * n

    while queue:
        v = queue.popleft()
        for i in graph[v]:
            if not visited[i]:
                queue.append(i)
                tmp.append(i)
                visited[i] = True
    return tmp

ret = [[0] * n for _ in range(n)]
for i in range(n):
    arr = bfs(i)
    for j in arr:
        ret[i][j] = 1

for a in ret:
    print(*a, sep=' ', end="\n")