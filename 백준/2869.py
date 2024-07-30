import sys

a, b, v = map(int, sys.stdin.readline().split())

# jump = a - b
# c_height = 0
# today = 0
# while c_height < v:
#     today += 1
#     if c_height + a >= v:
#         break
#     c_height += jump

# print(today)

# 시간 0.15초. -> 반복문을 사용하면 안된다.
# v-b = 올라가야할 거리
# a-b = 하루에 갈 수 있는 거리

# 올라가야할 거리 % 하루에 갈 수 있는 거리 == 0
# 나머지가 0 이면 낮 동안에 정상까지 갔다는 뜻
# 나머지가 0이 아니면 낮 동안에 정상까지 가지 못해 밤에 미끄러졌다는 뜻

if (v-b) % (a-b) == 0:
    print((v-b)//(a-b))
else:
    print((v-b)//(a-b)+1)