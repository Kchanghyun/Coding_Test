import sys
import copy
from itertools import combinations
from collections import deque

input = sys.stdin.readline

N, M = map(int, input().split())

city = [list(map(int, input().split())) for _ in range(N)]
result = 999999
chick = []
house = []
cnt = 0
for i in range(N):
    for j in range(N):
        if city[i][j] == 1:
            house.append([i, j])
        elif city[i][j] == 2:
            cnt += 1
            chick.append([i, j])

for chi in combinations(chick, M):
    temp = 0
    for h in house:
        chi_len = 999
        for j in range(M):
            chi_len = min(chi_len, abs(h[0] - chi[j][0]) + abs(h[1] - chi[j][1]))
        temp += chi_len
    result = min(result, temp)

print(result)

