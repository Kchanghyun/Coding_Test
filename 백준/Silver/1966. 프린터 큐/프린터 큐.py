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