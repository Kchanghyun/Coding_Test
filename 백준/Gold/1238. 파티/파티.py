import sys
import heapq

input = sys.stdin.readline

N, M, X = map(int, input().split())
graph = [[] for _ in range(N+1)]
reverse_graph = [[] for _ in range(N+1)]
heap = []
INF = sys.maxsize
dp = [INF] * (N+1)
reverse_dp = [INF] * (N+1)


for i in range(M):
    s, e, w = map(int, input().split())
    graph[s].append((w, e))
    reverse_graph[e].append((w, s))

def Dijkstra(start, arr, num):
    num[start] = 0
    heapq.heappush(heap, (num[start], start))

    while heap:
        wei, now = heapq.heappop(heap)

        if num[now] < wei:
            continue

        for w, next_node in arr[now]:
            next_wei = w + wei
            if num[next_node] > next_wei:
                num[next_node] = next_wei
                heapq.heappush(heap, (next_wei, next_node))


Dijkstra(X, graph, dp)
Dijkstra(X, reverse_graph, reverse_dp)

max = 0
for i in range(1, N+1):
    if max < dp[i] + reverse_dp[i]:
        max = dp[i] + reverse_dp[i]

print(max)