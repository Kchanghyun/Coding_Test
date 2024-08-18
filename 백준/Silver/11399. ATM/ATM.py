import sys

N = int(sys.stdin.readline())  # 5

time = list(map(int, sys.stdin.readline().split()))  # 3 1 4 3 2

ret = 0
tmp = 0
for i in sorted(time):
    tmp += i
    ret += tmp

print(ret)
