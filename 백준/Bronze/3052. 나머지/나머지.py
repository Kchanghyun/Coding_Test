a = [] * 10
b = []
for i in range(10):
    a.append(int(input()))
    if a[i] % 42 in b:
        continue
    b.append(a[i] % 42)

print(len(b))
