import sys

n = int(sys.stdin.readline())

a = {}

for i in range(n):
    x= int(sys.stdin.readline())

    if x in a:
        a[x] += 1
    else:
        a[x] = 1

sorted_a = {key : a[key] for key in sorted(a)}

for key, value in sorted_a.items():
    for i in range(value):
        print(key)