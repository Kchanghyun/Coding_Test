# import sys
# from collections import deque

# T = int(sys.stdin.readline())

# for i in range(T):
#     a, b = map(int, sys.stdin.readline().split())

#     visited = [False for i in range(10001)]
#     deq = deque()
#     deq.append([a, ''])
#     visited[a] = True

#     while deq:
#         num, command = deq.popleft()

#         if num == b:
#             print(command)
#             break

#         d = num * 2 % 10000
#         if not visited[d]:
#             visited[d] = True
#             deq.append([d, command + 'D'])

#         s = (num - 1) % 10000
#         if not visited[s]:
#             visited[s] = True
#             deq.append([s, command + 'S'])

#         l = num // 1000 + (num % 1000)*10
#         if not visited[l]:
#             visited[l] = True
#             deq.append([l, command + 'L'])

#         r = num // 10 + (num % 10) * 1000
#         if not visited[r]:
#             visited[r] = True
#             deq.append([r, command + 'R'])


import sys
from collections import deque

T = int(sys.stdin.readline())

for i in range(T):
    a, b = map(int, sys.stdin.readline().split())

    visited = [False for i in range(10001)]
    deq = deque()
    deq.append([a, ''])

    while deq:
        num, command = deq.popleft()

        if num == b:
            print(command)
            break

        d = num * 2 % 10000
        if not visited[d]:
            visited[d] = True
            deq.append([d, command + 'D'])

        s = (num - 1) % 10000
        if not visited[s]:
            visited[s] = True
            deq.append([s, command + 'S'])

        l = (num % 1000) * 10 + (num // 1000)
        # num % 1000을 통해 뒤 3자리 구한 다음 * 10으로 앞 3자리로 만들고, num // 1000 한 값을 더해주면서 기존 천의자리에 있던 값이 1의 자리로 가게 함.
        if not visited[l]:
            visited[l] = True
            deq.append([l, command + 'L'])

        r = num // 10 + (num % 10) * 1000
        if not visited[r]:
            visited[r] = True
            deq.append([r, command + 'R'])

