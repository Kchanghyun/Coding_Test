import sys

n = int(sys.stdin.readline())
m = int(sys.stdin.readline())
s = sys.stdin.readline().strip()

P = ('IO' * n) + 'I'
# print('P = {}'.format(P))
cnt = 0
for i in range(len(s)):
    if s[i] == 'I':
        # print('s[{}:{}+len(P)] = {}'.format(i, i, s[i:i+len(P)]))
        if s[i:i+len(P)] == P:
            cnt += 1

print(cnt)