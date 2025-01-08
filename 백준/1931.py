import sys

n = int(sys.stdin.readline())
meeting = []
for i in range(n):
    start, end = map(int, sys.stdin.readline().split())
    meeting.append((start, end))

meeting.sort(reverse=True)

opt_meeting = []
for x, y in meeting:
    z = y - x
    if len(opt_meeting) == 0:
        opt_meeting.append((x, y))
    elif opt_meeting[len(opt_meeting)-1][0] >= y:
        opt_meeting.append((x, y))

print(len(opt_meeting))
