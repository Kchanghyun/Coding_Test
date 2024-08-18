import sys

n = int(sys.stdin.readline())

point = []

for i in range(n):
    x, y = map(int, sys.stdin.readline().split())

    point.append((x,y))

for i in sorted(point, key=lambda x : (x[1], x[0])):
    print(i[0], i[1])