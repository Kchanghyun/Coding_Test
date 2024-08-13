from collections import deque

n, k = map(int, input().split())


def solution(n, k):
    if n >= k:
        return n - k

    q = deque()
    q.append([0, n])
    visited = [False] * (k * 2 + 1)
    while q:
        cost, pos = q.popleft()
        if pos == k:
            return cost

        for nxt in (pos - 1, pos + 1, pos * 2):
            if 0 <= nxt <= k + 1 and not visited[nxt]:
                visited[nxt] = True
                q.append((cost + 1, nxt))


print(solution(n, k))