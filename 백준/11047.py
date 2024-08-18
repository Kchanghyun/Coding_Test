import sys

n, k = map(int, sys.stdin.readline().split())

coin = []
count = 0
for i in range(n):
    coin.append(int(sys.stdin.readline()))

for i in sorted(coin, reverse=True):
    count += k // i
    k %= i


print(count)

