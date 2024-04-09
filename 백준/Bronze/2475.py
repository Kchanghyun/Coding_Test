a = list(map(int, input().split()))
ret = 0
# for i in range(0, len(a)):
#     ret += a[i] * a[i]
for i in a:
    ret += i ** 2
print(ret % 10)