import sys
input = sys.stdin.readline

num = input().strip()
isbn = 0
is_even = False
# 홀수는 그냥 더하고 짝수는 3배 값을 더하면 10의 배수가 나와야 함.
for i in range(len(num)):
    if num[i] == "*":
        if i % 2 != 0:
            is_even = True
        continue
    # a = int(num[i])
    # if a % 2 == 0:
    #     # 짝수라면
    #     isbn += a
    # elif a % 2 == 1:
    #     isbn += 3 * a
    isbn += int(num[i]) * (1 if i % 2 == 0 else 3)

if is_even:
    for i in range(10):
        if (isbn + (i * 3)) % 10 == 0:
            print(i)
            break
else:
    print(10 - isbn % 10)
