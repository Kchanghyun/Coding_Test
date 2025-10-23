"""
MST 시간복잡도 : O(E logE)
1. 아이디어
- MST 기본문제, 외우기
- 간선을 인접리스트에 집어넣기
- 힙에 시작점넣기
- 힙이 빌떄까지 다음의 작업을 반복
    - 힙의 최소값 꺼내서, 해당 노드 방문 안했다면
            - 방문표시, 해당비용 추가, 연결된 간선들 힙에 넣어주기
            
2. 시간복잡도
- MST : O(ElogE)

3. 자료구조
- 간선 저장 되는 인접리스트 : (무게, 노드번호)
- 힙 : (무게, 노드번호)
- 방문 여부 : bool[]
- MST 결과값 : int
"""""

import sys
import heapq

input = sys.stdin.readline

V, E = map(int, input().split())
edge = [[] for _ in range(V + 1)] # 인접 리스트로 만들려면 각각 빈 리스트를 하나씩 만들어줘야함

for i in range(E):
    A, B, C = map(int, input().split())
    edge[A].append([C, B])
    edge[B].append([C, A])

heap = [[0, 1]] # 시작점 지정해주지 않으면 시작 노드 상관 X
chk = [False] * (V+1)
rs = 0
while heap:
    w, next_node = heapq.heappop(heap)
    if not chk[next_node]:
        chk[next_node] = True
        rs += w
        for next_edge in edge[next_node]:
            if not chk[next_edge[1]]: # next_edge[0] = 무게, next_edge[1] = 시작 노드
                heapq.heappush(heap, next_edge)

print(rs)