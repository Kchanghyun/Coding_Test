import sys

x = int(sys.stdin.readline())

dp = [0] * (x+1)
# dp[1]은 0으로 이미 초기화되어있음

for i in range(2, x+1):
    dp[i] = dp[i-1] + 1 # 2 -> 1
    if i % 2 == 0:
        dp[i] = min(dp[i], dp[i//2] + 1) # dp[2] = 1, dp[1] + 1 = 1
    if i % 3 == 0:
        dp[i] = min(dp[i], dp[i // 3] + 1)  # dp[3] = 2, dp[1] + 1 = 1

print(dp[x])
