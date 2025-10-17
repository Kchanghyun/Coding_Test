import sys
input = sys.stdin.readline

N, M = map(int, input().split())
rs = []
chk = [False] * (N+1)


def recur(num):
    if num == M:
        print(' '.join(map(str, rs)))
        return
    for i in range(1, N+1):
        if not chk[i]:
            chk[i] = True
            rs.append(i)
            recur(len(rs))
            chk[i] = False
            rs.pop()


recur(0)

