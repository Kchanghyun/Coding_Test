import sys

m = int(sys.stdin.readline())
a = []

def calculate(input):
    global a
    x = input.split()
    if x[0] == 'all':
        a = [str(x) for x in range(1,21)]
        return
    elif x[0] == 'empty':
        a = []
        return
    elif x[1] in a:
        if x[0] == 'remove' or x[0] == 'toggle':
            a.remove(x[1])
        elif x[0] == 'check':
            print(1)
    else:
        if x[0] == 'add' or x[0] == 'toggle':
            a.append(x[1])
        elif x[0] == 'check':
            print(0)

for i in range(m):
    input = sys.stdin.readline()
    calculate(input)