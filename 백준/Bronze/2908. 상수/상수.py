a, b = map(str, input().split())

c = ''
d = ''
for i in range(0, 3):
    c += a[len(a) - i - 1]
    d += b[len(b) - i - 1]

if int(c) > int(d):
    print(c)
else:
    print(d)