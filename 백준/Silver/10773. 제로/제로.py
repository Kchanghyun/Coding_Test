import sys
k = int(sys.stdin.readline())
a = []
ret = 0
for i in range(k):
    num = int(sys.stdin.readline())
    ret += num
    if num == 0:
        tmp = a.pop()
        ret -= tmp
    else:
        a.append(num)
print(ret)
