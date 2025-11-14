import sys

input = sys.stdin.readline

t = int(input())

"""
새로운 리스트 변수 만들어서 각 값의 최대값을 계속 구해나가고, 그 변수 안의 최대값을 출력?
각 칸에서 선택할 수 있는 경우의 수
    1. 이번 스티커를 선택하지 않는다
        - 이전 열의 최대값을 가져옴
    2. 이번 열에서 윗줄 스티커를 선택
        - 직전 열의 아랫줄 스티커의 최대값을 가져옴
    3. 이번 열에서 아랫줄 스티커를 선
        - 직전 열의 윗줄 스티커의 최대값을 가져옴
        
"""

for i in range(t):
    n = int(input())
    arr = [list(map(int, input().split())) for _ in range(2)]
    dp = [[0] * n for _ in range(2)]

    dp[0][0] = arr[0][0]
    dp[1][0] = arr[1][0]

    if n == 1:
        print(max(dp[0][0], dp[1][0]))
        continue

    dp[0][1] = arr[1][0] + arr[0][1]
    dp[1][1] = arr[0][0] + arr[1][1]

    if n == 2:
        print(max(dp[0][1], dp[1][1]))
        continue

    for i in range(2, n):
        dp[0][i] = max(dp[1][i-2], dp[1][i-1]) + arr[0][i]
        dp[1][i] = max(dp[0][i-2], dp[0][i-1]) + arr[1][i]

    print(max(dp[0][-1], dp[1][-1]))
