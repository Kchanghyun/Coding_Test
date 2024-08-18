import sys

n, m = map(int, sys.stdin.readline().split())

a = {}
name = []

for i in range(n+m):
    input = sys.stdin.readline().strip()
    if input in a:
        a[input] += 1
    else:
        a[input] = 1

for k,v in sorted(a.items()):
    if v == 2:
        name.append(k)

print(len(name))
print(*name, sep='\n')