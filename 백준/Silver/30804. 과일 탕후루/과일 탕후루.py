import sys
from collections import defaultdict

n = int(sys.stdin.readline())
fruits = list(map(int, sys.stdin.readline().split()))

dict = defaultdict(int)
# 기본 dictiionary는 키가 존재하지 않을 때 오류가 나기 때문에 if문을 통해 존재하는지 여부를 파악해야 함.
# defaultdict는 키가 존재하지 않는 경우에도 자동으로 기본값(0)을 설정해주기 떄문에 추가적인 조건문을 작성할 필요가 없음.
left = 0
max_length = 0

for right in range(n):
    # 오른쪽 포인터가 가리키는 과일 추가
    dict[fruits[right]] += 1

    # 딕셔너리에 과일 종류가 3개 이상이면 윈도우 축소
    while len(dict) > 2:
        dict[fruits[left]] -= 1
        if dict[fruits[left]] == 0:
            del dict[fruits[left]] # 빈 과일 제거
        left += 1

    max_length = max(max_length, right - left + 1)


print(max_length)