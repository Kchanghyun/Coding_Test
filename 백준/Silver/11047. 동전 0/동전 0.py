import sys

input = sys.stdin.readline

N, K = map(int, input().split())

coins = []
cnt = 0
for i in range(N):
    coins.append(int(input()))

for coin in reversed(coins):
    if K == 0:
        break
    cnt += K // coin
    K %= coin

print(cnt)