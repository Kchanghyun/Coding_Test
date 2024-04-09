a = []
mul = 1
for i in range(0, 3):
    a.append(int(input()))
    mul *= a[i]
mul = list(str(mul))
for i in range(0, 10):
    print(mul.count(str(i)))