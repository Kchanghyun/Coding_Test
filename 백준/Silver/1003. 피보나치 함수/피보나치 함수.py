import sys

T = int(sys.stdin.readline())

memo = {0 : (1,0), 1: (0,1)}

def fibonacci(n):
    if n in memo:
        return memo[n]
    else:
        count_n1 = fibonacci(n-1)
        count_n2 = fibonacci(n-2)
        memo[n] = (count_n1[0] + count_n2[0], count_n1[1] + count_n2[1])
        return memo[n]


for i in range(T):
    n = int(sys.stdin.readline())
    zero_count, one_count = fibonacci(n)
    print(zero_count, one_count)