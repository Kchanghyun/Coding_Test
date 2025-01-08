import sys
from collections import deque

m, n = map(int, sys.stdin.readline().split())  # m * n 사이즈

box = []
for i in range(n):
    box.append(list(map(int, sys.stdin.readline().split())))

print(box)
# bfs 알고리즘 사용해서 -1을 제외하고 모두 1로 변하는데 걸리는 최소 일수 구하기.
# 단 -1부분때문에 모두 1로 만들지 못하는 경우에는 -1 출력하기

queue = deque()
visited = set()
def bfs(x, y):






    queue.append((x, y))
    visited.add((x, y))
    dx = [1, -1, 0, 0]
    dy = [0, 0, 1, -1]
    for i in range(4):
        cx = x + dx
        cy = y + dy
        if cx < 0:


count = 0
while True:
    if len(queue) == 0:
        break
    for a in range(n):
        for b in range(m):
            if box[a][b] == 1 and (a, b) not in visited:
                bfs(a, b)
    count += 1