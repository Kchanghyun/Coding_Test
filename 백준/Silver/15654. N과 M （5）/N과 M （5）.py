import sys

input = sys.stdin.readline

n, m = map(int, input().split())
num = list(map(int, input().split()))
num.sort()
ret = []


def recur():
    if len(ret) == m:
        print(*ret, sep=" ")
        return
    for i in num:
        if i not in ret:
            ret.append(i)
            recur()
            ret.pop()


recur()
