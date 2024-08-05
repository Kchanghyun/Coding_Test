import sys
from collections import deque

n = int(sys.stdin.readline())
line = int(sys.stdin.readline())
graph = {}

for i in range(line):
    x, y = map(int, sys.stdin.readline().split())
    if x not in graph:
        graph[x] = set()
    if y not in graph:
        graph[y] = set()

    graph[x].add(y)
    graph[y].add(x)


def bfs(start):
    count = 0
    visited = []
    queue = deque([start])
    visited.append(start)
    while queue:
        node = queue.popleft()
        if node in graph:
            for i in graph[node]:
                if i not in visited:
                    visited.append(i)
                    count += 1
                    queue.append(i)
    return count


print(bfs(1))
