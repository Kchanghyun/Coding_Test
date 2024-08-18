import sys

N, K = map(int, sys.stdin.readline().split())

def factorial(n):
    if n == 0:
        return 1
        # do something
    else:
        return n * factorial(n-1)

n = factorial(N)
r = factorial(K) * factorial(N-K)

print(n//r)