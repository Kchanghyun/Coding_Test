import sys

a, b = map(int, sys.stdin.readline().split())

x, y = a, b
# 최대공약수 구하는 방법
# 2개의 자연수 a,b에 대해서 a를 b로 나눈 나머지를 r이라 하면(단, a>b), a와 b의 최대공약수는 b와 r의 최대공약수와 같다.
# 유클리드 호제법(Euclidean Algorithm)
while True:
    r = x % y
    if r == 0:
        break
    x = y
    y = r

gcd = y
lcm = a * b // gcd

print(gcd)
print(lcm)