# import sys

# n = int(sys.stdin.readline())
# a = list(map(int, sys.stdin.readline().split()))

# m = int(sys.stdin.readline())
# b = list(map(int, sys.stdin.readline().split()))

# for i in b:
#     if i in a:
#         print(1)
#     else:
#         print(0)

# 이중 for문 또는 in을 사용해서 간단하게 해결할 수 있는 문제이지만, 이러한 방법을 사용할 경우
# 시간 초과 문제가 발생한다.
# 따라서 time complexity를 줄일 수 있는 이진 탐색(binary search)를 통해 문제를 해결한다.
# 이중 for문 또는 in을 사용한 경우의 time complexity는 O(NM)이고, 이진 탐색의 경우 O(MlogN)이라는 점에서,
# 이진 탐색의 time complexity가 더 작다는 것을 알 수 있다.

n = int(input())
n_list = list(map(int, input().split()))
n_list.sort()

m = int(input())
m_list = list(map(int, input().split()))

for i in m_list:
    start = 0
    end = n - 1

    while start <= end:
        mid = (start + end) // 2
        if i > n_list[mid]:
            start = mid + 1
        elif i < n_list[mid]:
            end = mid - 1
        else:
            start = mid
            end = mid
            break
    if start == mid and end == mid:
        print(1)
    else:
        print(0)
