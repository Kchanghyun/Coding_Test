import sys
from collections import defaultdict

n = int(sys.stdin.readline())
fruits = list(map(int, sys.stdin.readline().split()))

dict = defaultdict(int)
max_length = 0
left = 0

for right in range(n):
    dict[fruits[right]] += 1
    # print('right fruits[{}] = {}'.format(right, fruits[right]))
    if len(dict) > 2:
        # print('left fruits[{}] = {}'.format(left, fruits[left]))
        dict[fruits[left]] -= 1
        if dict[fruits[left]] == 0:
            del(dict[fruits[left]])
        left += 1
    # print(right)
    # print(dict)
    max_length = max(max_length, right - left + 1)

print(max_length)