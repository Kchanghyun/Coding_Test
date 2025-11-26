import sys

input = sys.stdin.readline

A = input().strip()
B = input().strip()

dp = [[0] * (len(B) + 1) for _ in range(len(A)+1)]

for i in range(1, len(A)+1):
    for j in range(1, len(B)+1):
        if A[i-1] == B[j-1]:
            dp[i][j] = dp[i-1][j-1] + 1
        elif A[i-1] != B[j-1]:
            dp[i][j] = max(dp[i-1][j], dp[i][j-1])

LCS = 0

for arr in dp:
    LCS = max(LCS, max(arr))

print(LCS)