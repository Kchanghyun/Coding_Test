n = int(input())

dp = [int(1e9)] * (n+1)
dp[0] = 0
for i in range(1, n+1):
    for j in range(1, int(n**0.5) + 1):
        square = j**2
        if square > i:
            break
        if square == i:
            dp[i] = 1
        dp[i] = min(dp[i], dp[i - square] + 1)
print(dp[n])
