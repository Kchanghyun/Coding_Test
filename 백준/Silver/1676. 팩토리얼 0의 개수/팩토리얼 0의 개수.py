n = int(input())
ret = 1
count = 0
for i in range(n, 0, -1):
    ret *= i

ret = reversed(list(str(ret)))
for i in ret:
    if i == '0':
        count += 1
    else:
        break
print(count)