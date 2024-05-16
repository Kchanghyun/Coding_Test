# k, n = map(int, input().split())
# a = []
# b = 0
# j = 1
# for _ in range(k):
#     a.append(int(input()))
#
# while True:
#     b = 0
#     for i in a:
#         b += i // j
#         if b > n:
#             break
#     if b == n-1:
#         j -= 1
#         break
#     j += 1
# print(j)

k, n = map(int, input().split())
a = [int(input()) for _ in range(k)]
start, end = 1, max(a)

while start <= end:
    ret = 0
    mid = (start + end) // 2
    for i in a:
        ret += i // mid

    if ret >= n:
        start = mid + 1
    else:
        end = mid - 1

print(end)
