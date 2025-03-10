import sys
from collections import deque

n = int(sys.stdin.readline())

deque = deque()
num = 0
for _ in range(n):
    command = sys.stdin.readline().strip().split()

    if len(command) > 1:
        num = int(command[1])

    if command[0] == 'push_back':
        deque.append(num)
    elif command[0] == 'push_front':
        deque.appendleft(num)
    elif command[0] == 'pop_front':
        print(deque.popleft() if deque else -1)
    elif command[0] == 'pop_back':
        print(deque.pop() if deque else -1)
    elif command[0] == 'size':
        print(len(deque))
    elif command[0] == 'empty':
        print(1 if not deque else 0)
    elif command[0] == 'front':
        print(deque[0] if deque else -1)
    elif command[0] == 'back':
        print(deque[len(deque)-1] if deque else -1)
