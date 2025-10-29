import sys

input = sys.stdin.readline

n = int(input())
nums = list(map(int, input().split()))

dp = [0] * n
dp[0] = nums[0]
# dp[0]에 nums[0] 저장 후

for i in range(1, n):
    dp[i] = max(nums[i], nums[i] + dp[i-1])
    # nums[i]와 nums[i] + dp[i-1] 값 중 최대값을 dp[i]에 저장
    # => dp[i]는 i 전까지의 값의 합 최대값을 가짐..?

print(max(dp))