import sys
from collections import deque
input = sys.stdin.readline

n = int(input())
tree = {}

for i in range(n-1):
    x, y = map(int, input().split())
    if x not in tree:
        tree[x] = [y]
    elif x in tree:
        tree[x].append(y)
    if y not in tree:
        tree[y] = [x]
    elif y in tree:
        tree[y].append(x)


def find_parents(root):
    parent = [0] * (n+1)
    visited = [False] * (n+1)
    q = deque([root])
    visited[root] = True

    while q:
        now = q.popleft()
        for nxt in tree[now]:
            if not visited[nxt]:
                parent[nxt] = now
                visited[nxt] = True
                q.append(nxt)
    return parent


parent = find_parents(1)

for i in range(2, n+1):
    print(parent[i])
