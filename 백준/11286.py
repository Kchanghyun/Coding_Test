import sys
import heapq
# 기본 힙은 최소 힙
n = int(sys.stdin.readline())

heap_q = []
for i in range(n):
    x = int(sys.stdin.readline())

    if x == 0:
        if len(heap_q) == 0:
            print(0)
        else:
            print(heapq.heappop(heap_q)[1])
    else:
        heapq.heappush(heap_q, (abs(x), x))





# import heapq

# heap_q = []

# heapq.heappush(heap_q, (abs(1), 1))
# heapq.heappush(heap_q, (abs(-1), -1))
# heapq.heappush(heap_q, (abs(-2), -2))

# print(heapq.heappop(heap_q)[1])
# print(heapq.heappop(heap_q)[1])
# print(heapq.heappop(heap_q)[1])

# 1 1 -1 -1 2 -2
# -> -1 -1 1 1 -2 2