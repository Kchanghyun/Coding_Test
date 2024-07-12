import sys

n = int(sys.stdin.readline())
point = []

for i in range(n):
    x, y = map(int, sys.stdin.readline().split())
    point.append((x,y))

for i in sorted(point):
    print(i[0], i[1])