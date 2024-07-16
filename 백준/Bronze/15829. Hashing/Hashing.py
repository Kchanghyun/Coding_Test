import sys

# a ~ z = 1 ~ 26
n = int(sys.stdin.readline())
string = sys.stdin.readline()

ret = 0
for i in range(n): # 0 ~ n-1
    alphabet = ord(string[i]) - 96
    ret += (alphabet * 31**i)

ret %= 1234567891
print(ret)
