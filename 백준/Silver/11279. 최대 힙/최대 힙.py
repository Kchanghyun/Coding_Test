import sys
import heapq

n = int(sys.stdin.readline())

heap_q = []
for i in range(n):
    x = int(sys.stdin.readline())
    if x == 0:
        if len(heap_q) == 0:
            print(0)
        else:
            tmp = heapq.heappop(heap_q)
            print(-tmp)
    else:
        heapq.heappush(heap_q, -x)

