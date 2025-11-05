import sys

input = sys.stdin.readline

n, m = map(int, input().split())
# n <= 1024, m <= 100000

# n 개의 줄은 주어지는 수
# m 개의 줄은 구해야 하는 좌표?

graph = [list(map(int, input().split())) for _ in range(n)]

S = [[0] * (n+1) for _ in range(n+1)]
for i in range(1, n+1):
    for j in range(1, n+1):
        S[i][j] = graph[i-1][j-1] + S[i-1][j] + S[i][j-1] - S[i-1][j-1]

for i in range(m):
    x1, y1, x2, y2 = map(int, input().split())
    # x1 <= x2, y1 <= y2
    # for j in range(x2-x1+1):
    #     for k in range(y2 - y1 + 1):
    #         ret += graph[x1+j-1][y1+k-1]
    ret = S[x2][y2] - S[x1-1][y2] - S[x2][y1-1] + S[x1-1][y1-1]
    print(ret)
