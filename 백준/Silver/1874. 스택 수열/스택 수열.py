n = int(input())
a = [int(input()) for _ in range(n)]
b = []
c = []
stack = []
j = 1
for i in a:
    while True:


        if j > i:
            c.append(stack.pop())
            b.append('-')
            break
        elif j <= i:
            stack.append(j)
            b.append('+')
            j += 1

if a != c:
    print('NO')
else:
    print(*b, sep='\n')