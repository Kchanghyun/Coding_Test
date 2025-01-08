import sys

n = int(sys.stdin.readline())

arr = list(map(int, sys.stdin.readline().split()))

arr2 = sorted(list(set(arr)))

dic = {arr2[i] : i for i in range(len(arr2))}
# arr[i]는 리스트 arr2의 i번째 요소를 가져온다.
# 딕셔너리의 키-값 쌍을 나타낸다. arr2[i]는 딕셔너리의 키가 되고, i는 해당 키의 값이 된다.
# {키: 값 for i in range(len(arr2))}는 반복문을 통해 여러 개의 키-값 쌍을 딕셔너리로 만들어준다.

for i in arr:
    print(dic[i], end=' ')
    