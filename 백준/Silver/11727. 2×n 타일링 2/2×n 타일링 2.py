import sys

n = int(sys.stdin.readline())

# 2 x 1 -> 1
# 2 x 2 -> 3
# 2 x 3 -> 5
# 2 x 4 -> 11
# 2 x 5 -> 21
# 2 x 6 -> 43

# dp[n] = dp[n-1] + 2 * dp[n-2]

dp = [0, 1, 3]
for i in range(3, n+1):
    dp.append(dp[i-1] + 2 * dp[i-2])

print(dp[n] % 10007)
