import sys

n = int(sys.stdin.readline())

meeting = []
for i in range(n):
    x, y = map(int, sys.stdin.readline().split())
    meeting.append((x, y))

meeting.sort(reverse=True)
count = []

for a, b in meeting:
    if len(count) == 0:
        count.append((a, b))
    # 이전 x 랑 다음 y랑 비교해서 y가 같거나 작으면 +1
    elif count[len(count)-1][0] >= b:
        count.append((a, b))

print(len(count))