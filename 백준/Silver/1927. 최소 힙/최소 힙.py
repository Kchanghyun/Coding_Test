import sys
import heapq

N = int(sys.stdin.readline())

heap_q = []
for i in range(N):
    x = int(sys.stdin.readline())
    if x == 0:
        if len(heap_q) == 0:
            print(0)
        else:
            print(heapq.heappop(heap_q))
    else:
        heapq.heappush(heap_q, x)