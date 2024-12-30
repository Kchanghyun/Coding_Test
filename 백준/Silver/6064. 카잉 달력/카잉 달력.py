import sys
import math

T = int(sys.stdin.readline())

for i in range(T):
    m, n, x, y = map(int, sys.stdin.readline().split())

    # x와 y가 n과 m 값을 넘어서기 전까지는 계속 같이 증가
    # x값이 m값보다 크거나 같으면 x = 1로 변경
    # y값도 n보다 크거나 같아지면 y = 1로 변경
    # ex) 첫번째 해 1:1
    # 두번째 해 2:2
    # 10번째 해 10:10
    # 11번째 해 1:11
    # ...
    year = x
    if (x-y) % math.gcd(m, n) != 0:
            year = -1
    while(year <= m * n):
        if year == -1:
             break
        if (year - x) % m == 0 and (year - y) % n == 0:
            break
        year += m
    print(year)