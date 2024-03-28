n, max = map(int, input().split())
a = list(map(int, input(). split()))
b = []
for i in range(0, n):
    if a[i] < max:
        b.append(a[i])  

print(' '.join(map(str, b)))