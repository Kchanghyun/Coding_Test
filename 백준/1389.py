import sys

INF = 987654321
n, m = map(int, sys.stdin.readline().split())

dist = [[INF] * n for _ in range(n)]
for i in range(n):
    dist[i][i] = 0

for i in range(m):
    a, b = map(int, sys.stdin.readline().split())

    dist[a-1][b-1] = 1
    dist[b-1][a-1] = 1


for k in range(n):
    # k는 거쳐가는 경우의 수
    for i in range(n):
        # i는 출발 정점
        for j in range(n):
            # j는 도착 정점
            # i -> k & k -> j
            if i == j:
                continue
            dist[i][j] = min(dist[i][j], dist[i][k] + dist[k][j])

# for i in dist:
#     print(*i, sep=' ')


d_min = INF
for i in range(n):
    n_sum = sum(dist[i])
    # print('n_sum = {}'.format(n_sum))
    # print(d_min)
    if d_min > n_sum:
        d_min = n_sum
        kevin_bacon = i+1 # 실제 정점은 배열 인덱스 값보다 +1임

print(kevin_bacon)