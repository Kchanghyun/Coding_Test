import sys
from collections import deque

N, K = map(int, sys.stdin.readline().split())

# 수빈 위치 : N
# 동생 위치 : K

# 1. 걸을 때 : x+1 or x-1
# 2. 순간이동 : 2x

# 동생 찾을 수 있는 가장 빠른 시간

def bfs(n, k):
    if n >= k:
        return n-k
    
    queue = deque()
    queue.append((n))
    MAX = 10 ** 5
    visited = [0] * (MAX + 1)

    while queue:
        cur = queue.popleft()
        if cur == k:
            return visited[k]
        
        for i in (cur-1, cur+1, cur*2):
            if 0 <= i <= MAX and not visited[i]:
                visited[i] = visited[cur] + 1
                queue.append(i)
    
print(bfs(N, K))