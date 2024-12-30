import sys

n, m = map(int, sys.stdin.readline().split())
# n - 사이트 주소의 수, m - 비밀번호를 찾으려는 사이트 주소의 수

memo = {}

for i in range(n):
    address, passwd = sys.stdin.readline().strip().split()

    memo[address] = passwd

for i in range(m):
    find_address = sys.stdin.readline().strip()
    print(memo[find_address])