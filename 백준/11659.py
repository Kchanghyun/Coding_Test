import sys

N, M = map(int, sys.stdin.readline().split())

N_list = list(map(int, sys.stdin.readline().split()))

prefix_sum = [0] * (N+1)
for i in range(1, N+1):
    prefix_sum[i] = prefix_sum[i-1] + N_list[i-1]

def range_sum(start, end):
    return prefix_sum[end] - prefix_sum[start-1]


for i in range(M):
    x, y = map(int, sys.stdin.readline().split())
    print(range_sum(x, y))