n = 6
a = list(map(int, input().split()))
b = [1, 1, 2, 2, 2, 8]
c = [0] * 6
print(a)
for i in range(0, len(a)):
    count = 0
    while a[i] != b[i]:
        if a[i] > b[i]:
            a[i] -= 1
            count -= 1
        else:
            a[i] += 1
            count += 1
    c[i] = count
print(' '.join(map(str, c)))
