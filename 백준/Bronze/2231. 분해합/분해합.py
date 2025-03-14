import sys

n = int(sys.stdin.readline())

def divsum(n):
    for i in range(1, n):
        x = str(i)
        a = i
        for j in x:
            a += int(j)
        if a == n:
            return i
    return 0

print(divsum(n))

# 분해합 경우의 수
# 1. 생성자가 없는 자연수의 경우 -> 생성자가 생긴다면 n의 값을 넘어버림. (ex : 0 or 1)
# 2. 생성자가 여러 개인 자연수의 경우