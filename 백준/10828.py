import sys

n = int(sys.stdin.readline())

stack_Array = []

def stack(n):
    if n[0] == 'push':
        stack_Array.append(int(n[1]))
    elif n[0] == 'pop':
        if len(stack_Array) == 0:
            print(-1)
        else:
            print(stack_Array.pop())
    elif n[0] == 'size':
        print(len(stack_Array))
    elif n[0] == 'empty':
        if len(stack_Array) == 0:
            print(1)
        else:
            print(0)
    elif n[0] == 'top':
        if len(stack_Array) == 0:
            print(-1)
        else:
            print(stack_Array[len(stack_Array) - 1])

for i in range(n):
    cmd = sys.stdin.readline().split()
    stack(cmd)