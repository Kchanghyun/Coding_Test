import sys

n = int(sys.stdin.readline())

user = []

for _ in range(n):
    age, name = input().split()
    user.append((int(age), name)) # 나이와 이름을 튜플로 묶어 리스트에 추가

# lambda 함수를 사용하여 리스트의 요소에서 나이를 추출하고 int형으로 변환
# user = sorted(user, key=lambda x : x[0])

# for age, name in user:
#     print(age, name)

for i in sorted(user, key=lambda x : x[0]):
    print(i[0], i[1])