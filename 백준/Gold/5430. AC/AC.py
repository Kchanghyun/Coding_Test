import sys
from collections import deque

t = int(sys.stdin.readline())

for i in range(t):
    p = list(sys.stdin.readline().strip())  # 수행할 함수
    n = int(sys.stdin.readline())  # 배열에 들어있는 수의 개수
    input_str = sys.stdin.readline().strip()  # 입력을 받음
    # 대괄호와 쉼표 제거
    cleaned_str = input_str.replace('[', '').replace(']', '').replace(',', ' ')
    # 숫자로 변환 후 리스트에 저장
    numbers = deque(list(map(int, cleaned_str.split())))

    end = 0
    count_R = 0
    for a in p:
        if a == 'R':
            count_R += 1
        elif a == 'D':
            if len(numbers) == 0:
                print("error")
                end = 1
                break
            else:
                if count_R % 2 == 0:
                    numbers.popleft()
                else:
                    numbers.pop()
    if end == 0:
        if count_R % 2 == 1:
            numbers.reverse()
        print('[', end='')
        print(*numbers, sep=',', end=']\n')