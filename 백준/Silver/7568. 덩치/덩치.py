import sys

n = int(sys.stdin.readline())
a = []

for i in range(n):
    x, y = map(int, sys.stdin.readline().split())

    a.append((x,y))

for i in range(n):
    result = 1
    for j in range(n):
        if a[i][0] < a[j][0] and a[i][1] < a[j][1]:
            result += 1
    print(result, end = ' ')
