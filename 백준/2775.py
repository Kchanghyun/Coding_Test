import sys

t = int(sys.stdin.readline())

# 0층 1호 = 1명
# 0층 2호 = 2명
# 0층 3호 = 3명
# 1층 1호 = 0층 1호 = 1명
# 1층 2호 = 0층1호 + 0층2호 = 1+2 = 3명
# 1층 3호 = 0층1호 + 0층2호 + 0층3호 = 1+2+3 = 6
# 2층 1호 = 1층 1호 = 1명
# 2층 2호 = 1층 1호 + 1층 2호 = 1+3 = 4명
# 2층 3호 = 1층 1호 + 1층 2호 + 1층 3호 = 1+3+6 = 10명

floor = [[0 for j in range(15)] for i in range(15)]

for i in range(15):
    count = 0
    for j in range(15):
        if i == 0:
            floor[i][j] = j+1
        else:
            count += floor[i-1][j]
            floor[i][j] = count
for i in range(t):
    k = int(sys.stdin.readline())
    n = int(sys.stdin.readline())
    print(floor[k][n-1])