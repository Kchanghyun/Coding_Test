a = list(map(int, input().split()))
ret = 0
for i in range(0, len(a)):
    ret += a[i] * a[i]
print(ret % 10)