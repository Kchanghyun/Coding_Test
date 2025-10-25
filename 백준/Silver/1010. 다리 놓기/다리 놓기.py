import sys
input = sys.stdin.readline

T = int(input())


def factorial(num):
    if num == 1 or num == 0:
        return 1
    return num * factorial(num-1)
    # n = 1
    # for k in range(1, num+1):
    #     n *= k
    # return n


for i in range(T):
    N, M = map(int, input().split())
    bridge = factorial(M) // (factorial(N) * factorial(M-N))
    print(bridge)

