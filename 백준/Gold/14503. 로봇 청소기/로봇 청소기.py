import sys

input = sys.stdin.readline

N, M = map(int, input().split())
r, c, d = map(int, input().split())
# d = 0 : 북쪽
# d = 1 : 동쪽
# d = 2 : 남쪽
# d = 3 : 서쪽

points = [(0, 1), (1, 0), (0, -1), (-1, 0)]

room = [list(map(int, input().split()))for _ in range(N)]
cnt = 0
# 0 -> 청소 x
# 1 -> 벽

# visited = [[False] * M for _ in range(N)]
# 청소 = 2로 변경

dy = [-1, 0, 1, 0]
dx = [0, 1, 0, -1]

while True:
    if room[r][c] == 0:
        room[r][c] = 2
        cnt += 1
    sw = False
    for i in range(1, 5):
        ny = r + dy[d-i]
        nx = c + dx[d-i]
        if 0 <= ny < N and 0 <= nx < M:
            if room[ny][nx] == 0:
                d = (d-i+4)%4
                r = ny
                c = nx
                sw = True
                break

    # 4방향 모두 x
    if not sw:
        # 후진 방향이 막혀있는 지 확인
        ny = r - dy[d]
        nx = c - dx[d]
        if 0 <= ny < N and 0 <= nx < M:
            if room[ny][nx] == 1:
                break
            else:
                r = ny
                c = nx
        else:
            break
print(cnt)