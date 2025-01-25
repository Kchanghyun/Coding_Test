import sys
import bisect

n = int(sys.stdin.readline())

a = list(map(int, sys.stdin.readline().split()))


def solved(seq):
    lis_array = []
    for num in seq:
        pos = bisect.bisect_left(lis_array, num)
        if pos == len(lis_array):
            lis_array.append(num)
        else:
            lis_array[pos] = num
    return len(lis_array)


print(solved(a))

# 5 2 8 6 3 6 9 7
# 1. 5
# 2. 2
# 3. 2 8
# 4. 2 6
# 5. 2 3
# 6. 2 3 6
# 7. 2 3 6 9
# 8. 2 3 6 7