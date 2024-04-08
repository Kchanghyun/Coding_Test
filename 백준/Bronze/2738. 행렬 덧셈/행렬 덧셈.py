n, m = map(int, input().split())
a = []

for i in range(n*2):
    a.append([])
    a[i] = list(map(int, input().split()))

for i in range(0, n):
    for j in range(0, m):
        print(a[i][j] + a[i+n][j], end=' ')
    print()