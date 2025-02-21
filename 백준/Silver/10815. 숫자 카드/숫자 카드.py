import sys

n = int(sys.stdin.readline())
card = set(map(int, sys.stdin.readline().split()))

m = int(sys.stdin.readline())
num = map(int, sys.stdin.readline().split())

ans = []

for x in num:
    if x in card:
        ans.append(1)
    else:
        ans.append(0)

print(*ans)