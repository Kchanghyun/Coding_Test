import sys
N, M, B = map(int, sys.stdin.readline().split())
# N: 세로, M: 가로, B: 인벤토리 속 블록 수
a = []
mxcnt = 0
mncnt = 0

for i in range(N):
    tmp = list(map(int, sys.stdin.readline().split()))
    a.append(tmp)

heights = [block for row in a for block in row] # 모든 블록의 높이를 1차원 리스트로 변환
heights.sort() # 1차원 배열의 정렬

cnt = heights.count(heights[0])
if cnt >= 1:
    for i in range(cnt):
        heights[i] += 1
        mxcnt += 1
        mncnt += 1

mn = min(heights)
mx = max(heights)

for i in heights:
    if mx > i:
        mxcnt += mx - i
    if mn < i:
        mncnt += (i - mn) * 2

if mncnt < mxcnt or B - mxcnt < 0:
    print(mncnt, mn)

else:
    print(mxcnt, mx)

