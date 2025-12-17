import sys
from itertools import combinations

input = sys.stdin.readline

N, M = map(int, input().split())

graph = [list(map(int, input().split())) for _ in range(N)]
city = []
chicken = []

for i in range(N):
    for j in range(N):
        if graph[i][j] == 1:
            city.append([i, j])
        elif graph[i][j] == 2:
            chicken.append([i, j])

result = 999999
for chi in combinations(chicken, M):
    temp = 0
    # 3개 조합 뽑았으니까 1있던 곳 for문으로 돌면서 가장 가까운 2의 치킨거리 구하기
    for i in city:
        chi_len = 999
        for j in range(M):
            chi_len = min(chi_len, abs(i[0] - chi[j][0]) + abs(i[1] - chi[j][1]))
        temp += chi_len
    result = min(temp, result)

print(result)