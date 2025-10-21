""""
1. 아이디어
- N개의 숫자를 정렬
- M개를 for 돌면서, 이진탐색
- 이진탐색 안에서 마지막에 데이터 찾으면, 1출력, 아니면 0출력

2. 시간복잡도
- N개 입력값 정렬 = O(NlogN)
- M개를 N개 중에서 탐색 = O(M * logN)
- 총합 : O((N+M)logNM) > 가능

3. 자료구조
- N개 숫자 : int[]
- M개 숫자 : int[]
"""""

import sys

input = sys.stdin.readline

N = int(input())
A = list(map(int, input().split()))
M = int(input())
nums = list(map(int, input().split()))


def search(st, en, target):
    while st <= en:
        mid = (st + en) // 2
        if A[mid] == target:
            print(1)
            return
        if A[mid] < target:
            st = mid+1
        else:
            en = mid-1
    print(0)



A.sort()
for a in nums:
    # list의 a in A는 맨 앞에서부터 순차적으로 찾는다.
    # -> 완전탐색과 동일 > O(N)
    # if a in A:
    #     print(1)
    # else:
    #     print(0)
    search(0, len(A) - 1, a)