import sys

n, m, b = map(int, sys.stdin.readline().split())
mat = [list(map(int, sys.stdin.readline().split())) for _ in range(n)]

lo = min([min(x) for x in mat]) # mat 리스트 중 제일 낮은 땅의 높이
hi = max([max(x) for x in mat]) # mat 리스트 중 제일 높은 땅의 높이
INF = int(1e9)

def check(mat, lv, b):
    # lv마다 걸리는 시간 -> return -> 불가능 시 INF return
    sc = 0
    c = 0 # lv보다 낮은 높이의 땅을 채워넣어야 하는 블록의 개수
    for i in range(n):
        for j in range(m):
            z = mat[i][j] - lv
            if z > 0: # lv보다 mat[i][j]값이 크다면
                b += z # 인벤토리 안에 블록 집어넣음
                sc += 2*z # 블록을 제거하는데 걸리는 시간
            else:
                c += -z
    if b < c:
        return INF
    return sc + c # sc는 블록을 제거하는데 걸리는 시간만 추가했음.
    # 함수에서 모든 경우에 사용할 수 있게 c(블록을 쌓는데 걸리는 시간)도 추가해줘야 함.

msc = INF # minimum second
mlv = 0 # maximum level
for lv in (range(hi, lo-1, -1)):
    sc = check(mat, lv, b)
    if msc > sc: # 이미 가장 높은 층 블록부터 for문을 돌았기 때문에 같은 시간이 걸린다면 가장 높은 lv일 때 값이 답으로 출력됨.
        msc = sc
        mlv = lv

print(msc, mlv)


import sys

n, m, b = map(int, sys.stdin.readline().split())
ground = []

for i in range(n):
    ground.append(list(map(int, sys.stdin.readline().split())))

time = [0 for i in range(257)] # time[k]에 땅높이가 k일 때의 소요시간 저장
height = 0
for g in range(257):
    block = b # 인벤토리에 남은 블록 수
    for i in ground:
