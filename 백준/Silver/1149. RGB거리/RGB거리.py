import sys

n = int(sys.stdin.readline())

rgbs = []
for i in range(n):
    rgbs.append(list(map(int, sys.stdin.readline().split())))

for i in range(1, n):
    rgbs[i][0] = min(rgbs[i-1][1], rgbs[i-1][2]) + rgbs[i][0]
    rgbs[i][1] = min(rgbs[i-1][0], rgbs[i-1][2]) + rgbs[i][1]
    rgbs[i][2] = min(rgbs[i-1][0], rgbs[i-1][1]) + rgbs[i][2]

print(min(rgbs[n-1][0], rgbs[n-1][1], rgbs[n-1][2]))
