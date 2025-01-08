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

# 인수 분해 했을 때 5의 개수 = 0의 개수
# n = int(input())
#
#
# def five_count(n):
#     cnt = 0
#     while n != 0:
#         n //= 5
#         cnt += n
#     return cnt
#
#
# print(five_count(n))
