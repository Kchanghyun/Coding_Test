import sys
from collections import deque

N, K = map(int, sys.stdin.readline().split())

# visited = {} 
# set이나 dictionary를 사용하면 메모리 사용량이 많다. 메모리 양이 적어야 할 때는 list를 쓰기

def bfs(n):
    q = deque()
    q.append(n)
    MAX = 10 ** 5
    visited = [0] * (MAX+1)

    while q:
        cur = q.popleft()
        if cur == K:
            return visited[K]
        
        for i in (cur-1, cur+1, cur*2):
            if 0 <= i <= MAX and not visited[i]:
                visited[i] = visited[cur] + 1
                q.append(i)
print(bfs(N))
