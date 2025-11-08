import sys

input = sys.stdin.readline

n, m = map(int, input().split())
num = sorted(list(map(int, input().split())))
ret = []

def recur():
    chk = 0
    if len(ret) == m:
        print(*ret)
        return
    for i in range(n):
        if chk != num[i] and (not ret or ret[-1] <= num[i]):
            ret.append(num[i])
            chk = num[i]
            recur()
            ret.pop()

recur()