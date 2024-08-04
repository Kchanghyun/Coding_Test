n = int(input())
a = [] # input data
b = [] # 1~n
c = [] # result data
for i in range(n):
    a.append(int(input()))
    b.append(i + 1)

tmp = 0
for i in a:
    while tmp != i:
          