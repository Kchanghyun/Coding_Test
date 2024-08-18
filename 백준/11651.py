import sys

n = int(sys.stdin.readline())

point = []

for i in range(n):
    x, y = map(int, sys.stdin.readline().split())

    point.append((x,y))

for i in sorted(point, key=lambda x : (x[1], x[0])): # y좌표 우선으로 정렬하다 y좌표 값(x[1])이 같다면 x좌표 값(x[0])으로 정렬
    print(i[0], i[1])