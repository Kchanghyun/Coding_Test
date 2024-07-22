import sys

n = int(sys.stdin.readline())

# 3킬로 or 5킬로
count = 5000
for i in range((n//5)+1):
    for j in range((n//3)+1):
        tmp = 5*(i) + 3*(j)
        if tmp == n and count > i+j:
            count = i + j
if count == 5000:
    count = -1
print(count)