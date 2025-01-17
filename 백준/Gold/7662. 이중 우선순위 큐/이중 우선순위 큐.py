import sys
import heapq


def isEmpty(nums):
    for item in nums:
        if item[1] > 0:
            return False
    return True


t = int(sys.stdin.readline())

for i in range(t):
    k = int(sys.stdin.readline())
    min_heap = []
    max_heap = []
    nums = {}

    for j in range(k):
        command, num = sys.stdin.readline().split()
        num = int(num)

        if command == 'I':
            if num in nums:
                nums[num] += 1
            else:
                heapq.heappush(min_heap, num)
                heapq.heappush(max_heap, -num)
                nums[num] = 1
        elif command == 'D':
            if not isEmpty(nums.items()):
                if num == 1:
                    while -max_heap[0] not in nums or nums[-max_heap[0]] < 1:
                        temp = -heapq.heappop(max_heap)
                        if temp in nums:
                            del(nums[temp])
                    nums[-max_heap[0]] -= 1
                else:
                    while min_heap[0] not in nums or nums[min_heap[0]] < 1:
                        temp = heapq.heappop(min_heap)
                        if temp in nums:
                            del(nums[temp])
                    nums[min_heap[0]] -= 1

    if isEmpty(nums.items()):
        print('EMPTY')
    else:
        while min_heap[0] not in nums or nums[min_heap[0]] < 1:
            heapq.heappop(min_heap)
        while -max_heap[0] not in nums or nums[-max_heap[0]] < 1:
            heapq.heappop(max_heap)
        print(-max_heap[0], min_heap[0])