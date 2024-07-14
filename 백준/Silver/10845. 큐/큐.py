import sys

n = int(sys.stdin.readline())
queue_array = []

def queue(a):
    if a[0] == 'push':
        queue_array.append(int(a[1]))
    elif a[0] == 'pop':
        if len(queue_array) == 0:
            print(-1)
        else:
            print(queue_array.pop(0))
    elif a[0] == 'size':
        print(len(queue_array))
    elif a[0] == 'empty':
        if len(queue_array) == 0:
            print(1)
        else:
            print(0)
    elif a[0] == 'front':
        if len(queue_array) == 0:
            print(-1)
        else:
            print(queue_array[0])
    elif a[0] == 'back':
        if len(queue_array) == 0:
            print(-1)
        else:
            print(queue_array[len(queue_array)-1])


for i in range(n):
    cmd = sys.stdin.readline().split()
    queue(cmd)