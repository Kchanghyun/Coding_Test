import sys
from collections import deque

n = int(sys.stdin.readline())

queue = deque(range(1, n+1))

while len(queue) != 1:
    queue.popleft()
    queue.rotate(-1)

print(queue[0])