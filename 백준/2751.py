import sys

n = int(sys.stdin.readline())
a = []
for i in range(n):
    a.append(int(sys.stdin.readline()))

a.sort()
print(*a, sep='\n')