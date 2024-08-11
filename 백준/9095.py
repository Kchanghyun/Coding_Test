import sys

T = int(sys.stdin.readline())

dp = [0, 1, 2, 4]

# dp[1] = 1
# dp[2] = 2
# dp[3] = 4
# dp[4] = 7
# dp[5] = 13
# dp[6] = 24
# dp[7] = 44
# ~~~

# dp[7] = dp[6] + dp[5] + dp[4]
# dp[6] = dp[5] + dp[4] + dp[3]

for _ in range(T):
    n = int(sys.stdin.readline())

    if len(dp) <= n:
        for i in range(len(dp), n+1):
            dp.append(dp[i-1] + dp[i-2] + dp[i-3])

    print(dp[n])