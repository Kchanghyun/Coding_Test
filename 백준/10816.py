import sys

M = int(sys.stdin.readline())
a = list(map(int, sys.stdin.readline().split()))


N = int(sys.stdin.readline())
b = list(map(int, sys.stdin.readline().split()))

count_card = {}
for n in a:
    if n in count_card:
        count_card[n] += 1
    else:
        count_card[n] = 1

def binarySearch(arr, x):
    left, right = 0, len(arr)-1
    result = 0
    while left <= right:
        mid = (left + right) // 2
        if arr[mid] == x:
            result = count_card[x]
            break
        elif arr[mid] > x:
            right = mid - 1
        else:
            left = mid + 1
    return result

# 성공!!
# for m in b:
#     if m in count_card:
#         print(count_card[m], end=' ')
#     else:
#         print(0, end=' ')
a.sort()
for m in b:
    print(binarySearch(a, m), end=' ')