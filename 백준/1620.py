import sys
n, m = map(int, sys.stdin.readline().split())

poketmon = {}
number = {}
for i in range(1,n+1):
    x = sys.stdin.readline().strip()
    poketmon[i] = x
    number[x] = i


for i in range(m):
    problem = sys.stdin.readline().strip()

    if problem.isdigit(): # 이건 숫자인지 파악하는거
        print(poketmon[int(problem)])
    else: # isalpha는 알파벳인지 파악하는 함수
        print(number[problem])

# a = '12'
# if a.isdigit():
#     print('yes')
# else:
#     print('no')
# -> yes