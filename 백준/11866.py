from collections import deque
import sys

def josephus_problem(n,k):
    # 1부터 n까지의 숫자를 가진 deque 생성
    queue = deque(range(1, n+1))
    result = []

    while queue:
        # k-1번 왼쪽으로 회전하여 k번째 요소가 맨 앞에 오게 함
        queue.rotate(-(k-1))
        # 맨 앞의 요소를 제거하고 결과 리스트에 추가
        result.append(queue.popleft())

    return result

n, k = map(int, sys.stdin.readline().split())

result = josephus_problem(n, k)

print('<',', '.join(map(str, result)), '>', sep='')
# map(str, result) <- result 리스트의 모든 요소를 문자열로 변환
# ', '.join 이 부분은 문자열 리스트를 쉼표와 공백으로 연결하여 하나의 문자열로 만든다.
# print('<', ..., '>', sep='') 이 부분은 print 함수의 여러 인자를 공백 없이 출력하려면 sep=''를 사용한다.