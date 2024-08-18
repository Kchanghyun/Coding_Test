import sys

T = int(sys.stdin.readline())

for i in range(T):
    VPS = sys.stdin.readline()
    left = 0
    right = 0
    for j in VPS:
        if j == '(':
            left += 1
        elif j == ')':
            right += 1
        if right > left:
            break
    if left == right:
        print('YES')
    else:
        print('NO')
