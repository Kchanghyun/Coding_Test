import sys

N, r, c = map(int, sys.stdin.readline().split())
# 2^N X 2^N
# print(arr[r][c])
r += 1
c += 1
ans = 0
while N != 0:
    N -= 1

    # 2 1
    # 3 4
    
    # 2사분면
    if r <= 2 ** N and c <= 2 ** N:
        ans += ((2 ** N) ** 2) * 0
    # 1사분면
    elif r <= 2 ** N and c > 2 ** N:
        ans += ((2 ** N) ** 2) * 1
        c -= (2 ** N)
    # 3사분면
    elif r > 2 ** N and c <= 2 ** N:
        ans += ((2 ** N) ** 2) * 2
        r -= (2 ** N)
    # 4사분면
    else:
        ans += ((2 ** N) ** 2) * 3
        r -= (2 ** N)
        c -= (2 ** N)

print(ans)