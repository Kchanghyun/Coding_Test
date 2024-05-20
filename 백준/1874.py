# n = int(input())

# # 입력받은 수열
# a = [int(input()) for _ in range(n)]

# # push(+)와 pop(-)를 저장해 둘 리스트
# b = []

# # push로 저장할 수열
# stack = []

# # pop을 통해 뽑아낸 수열
# c = []

# j = 1
# for i in a:
#     while True:


#         if j > i:
#             c.append(stack.pop())
#             b.append('-')
#             break
#         elif j <= i:
#             stack.append(j)
#             b.append('+')
#             j += 1

# if a != c:
#     print('NO')
# else:
#     print(*b, sep='\n')

n = int(input())

count = 1
stack = []
a = []
temp = True

for i in range(n):
    num = int(input())

    while count <= num:
        stack.append(count)
        a.append('+')
        count += 1

    if stack[-1] == num:
        stack.pop()
        a.append('-')
    else:
        temp = False
if temp == False:
    print('NO')
else:
    print(*a, sep='\n')