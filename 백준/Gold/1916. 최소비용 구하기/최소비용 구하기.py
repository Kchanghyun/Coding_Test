import sys
import heapq

input = sys.stdin.readline

N = int(input())
M = int(input())

graph = [[] * (N+1) for _ in range(N+1)]
visited = [False] * (N+1)
INF = 1e8
distances = [INF] * (N+1)

for i in range(M):
    s, e, w = map(int, input().split())
    graph[s].append((e, w))

s, e = map(int, input().split())

"""
시간제한 0.5초
대충 1억번 연산인가? 파이썬은 그보다 좀 느리니까 5천번??

N = 1000
M = 100000

A번째 도시에서 B번째 도시까지 가는데 드는 최소 비용
s에서 e까지 가는데 드는 최소 비용
"""

def dijkstra(graph, start):
    distances[start] = 0
    pq = [(0, start)] # 시작점 설정

    while pq:
        current_distance, current_node = heapq.heappop(pq)

        if current_distance > distances[current_node]:
            continue

        for neighbor, weight in graph[current_node]:
            distance = current_distance + weight

            if distance < distances[neighbor]:
                distances[neighbor] = distance
                heapq.heappush(pq, (distance, neighbor))
    return distances

result = dijkstra(graph, s)

print(result[e])