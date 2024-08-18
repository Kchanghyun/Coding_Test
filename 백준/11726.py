import sys

# 1 = 1
# 2 = 2
# 3 = 3
# 4 = 5
# 5 = 8
# 6 = 13

# i = i-1 + i-2

n = int(sys.stdin.readline())
dp = [0, 1, 2]

for i in range(3, n+1):
    dp.append(dp[i-1] + dp[i-2])

print(dp[n] % 10007)
