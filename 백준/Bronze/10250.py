# t = int(input())
# for i in range(0, t):
#     h, w, n = map(int, input().split())
#     room = str((n // h) + 1)
#     if int(room) < 10:
#         room = '0' + room
#     floor = str(n % h)
#     print(int(floor + room))

# n번째 손님 % H = 배정받은 층수
# (n번째 손님 / H) + 1 = 배정받은 호수
# 6층일 때 6번째로 오는 경우 저 공식대로라면 0이 나옴..

t = int(input())

for i in range(t):
    h, w, n = map(int, input().split())

    floor = (n % h)
    room = (n // h) + 1
    if floor == 0:
        floor = h
        room -= 1
    print(floor * 100 + room)