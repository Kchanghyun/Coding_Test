N = int(input())
N_list = list(map(int, input().split()))
N_list.sort()

M = int(input())
M_list = list(map(int, input().split()))

for m in M_list:
    left = 0
    right = N - 1

    while left <= right:
        mid = (left + right) // 2
        if m > N_list[mid]:
            left = mid + 1
        elif m < N_list[mid]:
            right = mid - 1
        else:
            left = mid
            right = mid
            break
    if left == mid and right == mid:
        print(1)
    else:
        print(0)

