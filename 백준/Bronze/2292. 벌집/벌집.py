import sys

n = int(sys.stdin.readline())

# 1 ( 1개 )
# 2 3 4 5 6 7 ( 6개 )
# 8 9 10 11 12 13 14 15 16 17 18 19 ( 12개 )
# 20 ~ 37 ( 18개 )
# 38 ~ 61 ( 24개 )
# 62 ~ 91 ( 30개 )

# 6의 배수?
# 6 * 0, 6 * 1, 6 * 2, 6 * 3 ...

count = 0
a = 1
for i in range(n):
    a += (6 * i)
    if a >= n:
        count = i + 1
        break
print(count)