import sys
from collections import deque

n, m = map(int, sys.stdin.readline().split())

# n - 사다리의 수, m - 뱀의 수

ladder = {start: end for start, end in [map(int, sys.stdin.readline().split()) for _ in range(n)]}
snake = {start: end for start, end in [map(int, sys.stdin.readline().split()) for _ in range(m)]}


# 1번 칸에서 100번 칸까지 도착하기 위해 주사위 굴리는 최소 횟수 구하기
# 사다리 - [0]에서 [1]로 이동 : 위로 이동
# 뱀 - [0]에서 [1]로 이동 : 아래로 이동

user = 1 # 처음 시작 1번 칸
finish = 100

dice = [1,2,3,4,5,6]
INF = int(1e9)


game = [INF for i in range(101)]
game[1] = 0
deq = deque([1])

while deq:
    x = deq.popleft()

    for i in dice:
        dx = x + i

        if dx > 100:
            continue
        if dx in snake:
            dx = snake[dx]
        if dx in ladder:
            dx = ladder[dx]

        if dx == 100:
            print(game[x] + 1)
            sys.exit(0)

        if game[dx] == INF:
            game[dx] = game[x] + 1
            deq.append(dx)

print(game[100])