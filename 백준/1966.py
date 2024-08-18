Documents = int(input())

for i in range(Documents):
    N, M = map(int, input().split())
    a = list(map(int, input().split()))

    result = 1
    while a:
        if a[0] < max(a):
            a.append(a.pop(0))
        else:
            if M == 0: break

            a.pop(0)
            result += 1
        M = M - 1 if M > 0 else len(a) - 1 # deque할 때마다 index 수정

    print(result)

    # 2 3 4 1 - 1
    # 3 4 1 2 - 0
    # 4 1 2 3 - 3
    # 1 2 3 - 2, result++
    # 2 3 1 - 1
    # 3 1 2 - 0
    # result = 2

    # 1 9 1 1 1 1 - 5
    # 9 1 1 1 1 1 - 4
    # 1 1 1 1 1 - 3, result++
    # 1 1 1 1 - 2, result++
    # 1 1 1 - 1, result++
    # 1 1 - 0, result++
    # result = 5